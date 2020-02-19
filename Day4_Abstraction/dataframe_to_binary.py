"""
dataframe_to_binary.py
Author: Nicholas A. Del Grosso

some functions that convert dataframes to a basic binary file format.  
An example of What Not To Do (TM) and part of an explanation of "binary"
as a format in general.
"""

from typing import *
import struct
import pandas as pd

class BinaryFormatter(NamedTuple):
    header: str
    body: str

def rec_dtype_to_struct_fmt(rec) -> str:
    return "".join(f[0].char for f in rec.dtype.fields.values())

def rec_fields_to_struct_fmt(rec):
    return "".join(str(len(s))+"s" for s in rec.dtype.fields)


def to_binary_file(df: pd.DataFrame, filename: str) -> BinaryFormatter:
    """
    Saves the dataframe to file, and also returns a BinaryFormatter containnig the Struct
    format string of the header and body of the file for later reading.
    """
    recs = df.to_records(index=False)
    body_fmt = rec_dtype_to_struct_fmt(recs)
    body = recs.tobytes()
    header_fmt = rec_fields_to_struct_fmt(recs)
    header = "".join(recs.dtype.fields).encode()
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(body)
    return BinaryFormatter(header=header_fmt, body=body_fmt)


def from_binary_file(filename: str, formatter: BinaryFormatter) -> pd.DataFrame:
    with open(filename, 'rb') as f:
        header = f.read(struct.calcsize(formatter.header))
        body = f.read()
    return pd.DataFrame(
        data=list(struct.iter_unpack(formatter.body, body)),
        columns=[s.decode() for s in struct.unpack(formatter.header, header)]
    )
    
