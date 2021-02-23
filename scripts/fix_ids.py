#!/usr/bin/python

import csv

# Run Run from ADH_and_ALDH_regulatory_networks/ directory

# The RsMergeArch.bcp.gz file (ftp://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606_b151_GRCh38p7/database/organism_data/RsMergeArch.bcp.gz)
# with rs merge table for genome GRCh38p7 build 151 was downloaded from the dbSNP ftp site
# (ftp://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606_b151_GRCh38p7/database/organism_data/) on 27/08/2020.

# This code adds "rs" to the old and new IDs in the RsMergeArch.bcp file and returns them.

to_replace = []
with open("data/RsMergeArch.bcp", 'r') as f:
    snp_reader = csv.reader(f, delimiter='\t')
    for row in snp_reader:
        snp_ids = row[:2]
        new_snp_ids = []
        for snp in snp_ids:
        	snp = "rs" + snp
        	new_snp_ids += [snp]
        to_replace.append(new_snp_ids)

# The first column is the merged old SNP rsID. The second column is a new one.
with open("data/RsMergeArch_rs.txt", 'w') as w:
	writer = csv.writer(w, delimiter='\t')
	writer.writerows(to_replace)


# The code accepts your table, reads the first column with rsIDs and checks if the SNP ID is old merged
# and create a new column with replaced rsIDs.

#with open('results/gwas/gwas_5E-08_snpsfixed_traitfixed.txt') as f:
#	snp_to_test = [line.split()[0] for line in f]

#data = pd.read_csv("data/RsMergeArch_rs.txt", sep="\t", header=None)
#df = pd.DataFrame (data, columns = ["old_rsID", "new_rsID"])
#df_dict = df.to_dict()

with open("data/RsMergeArch_rs.txt", 'r') as x:
    old_ids = [line.split()[0] for line in x]

with open("data/RsMergeArch_rs.txt", 'r') as y:
    new_ids = [line.split()[1] for line in y]

id_dict = {}
for i in range(len(old_ids)):
    id_dict[old_ids[i]] = new_ids[i]

with open("results/gwas/gwas_5E-08_snpsfixed_traitfixed.txt", 'r') as f:
    snp_reader = csv.reader(f, delimiter='\t')
    new_rows_list = []
    for row in snp_reader:
    	new_row = []
        if row[0] in old_ids:
        	r = id_dict.get(row[0])
        	new_row = [row[0], row[1], row[2], r]
        	print("Printing new row... ", new_row)
        	new_rows_list.append(new_row)
        else:
        	new_row = [row[0], row[1], row[2], row[0]]
        	new_rows_list.append(new_row)

with open("results/gwas/gwas_5E-08_snpsfixed_traitfixed_idfixed.txt", 'w') as w:
    writer = csv.writer(w, delimiter='\t')
    writer.writerows(new_rows_list)
