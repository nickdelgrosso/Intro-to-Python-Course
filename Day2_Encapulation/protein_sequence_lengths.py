dimport os
from os import path
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Bio.Seq import Seq
from Bio import SeqIO

## ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz

current_directory = os.getcwd()
session_path = path.join(current_directory, "MyExperiment", "data", "sessions")
all_files = os.listdir(session_path)
idx = 0
idx2 = 0

sequence_files = []
while idx < len(all_files):
    file = all_files[idx]
    filename, extension = path.splitext(file)
    if 'fasta' in extension.lower():
        sequence_files.append(file)
    idx = idx + 1
sequence_ids = []

sequences = []
for sequence_file in sequence_files:
    for seq_record in SeqIO.parse(sequence_file, "fasta"):
        id = seq_record.id
        
        sequence = seq_record.seq
        sequences.append(sequence)
        sequence_ids.append(id)
while idx2 < len(sequences):
    sequence = sequences[idx2]
    sequence_id = sequence_ids[idx2]
    print("Sequence ID: {}; Length: {}".format(sequence_id, len(sequence))
          
          