from Bio import SeqIO
import os

input_fasta = "/data/internship_data/nidhi/aba/new_output/extraction/genes/blaNDM-1.fasta"  
output_dir = "/data/internship_data/nidhi/aba/new_output/extraction/split_samples/blaNDM-1"

os.makedirs(output_dir, exist_ok=True)

for record in SeqIO.parse(input_fasta, "fasta"):
    sample_id = record.id
    output_path = os.path.join(output_dir, f"{sample_id}.fasta")
    
    with open(output_path, "w") as out:
        SeqIO.write(record, out, "fasta")
