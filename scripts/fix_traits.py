#!/usr/bin/python

import csv

# This script splits the line with multiple traits by ", ", creates a new line and 
# populates it with the same content as for unsplitted line except the mapped trait
# Run from ADH_and_ALDH_regulatory_networks/ directory

snps_file = "results/gwas/gwas_5E-08_snpsfixed.txt"
newfile = "results/gwas/gwas_5E-08_snpsfixed_traitfixed.txt"


with open(snps_file, 'r') as f:
    snps_file_reader = csv.reader(f, delimiter='\t')
    new_rows_list = []
    for row in snps_file_reader:
        new_row = []
        traits = row[2].split(", ")
        for trait in traits:
            new_row = [row[0], row[1], trait]
            new_rows_list.append(new_row)

with open(newfile, 'w') as w:
    writer = csv.writer(w, delimiter='\t')
    writer.writerows(new_rows_list)