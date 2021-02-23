#!/bin/bash

#hg38
FILE=$(pwd)/human_9606_b151_GRCh38p7.bed
DIR=$(pwd)/rsID2Bed
SNPs=$(pwd)/$1
echo Proccesing file:
echo $SNPs 

#check if working folder exist, if not, create

if [ ! -d $DIR ]
then
mkdir rsID2Bed
fi

cd rsID2Bed

#check if dbsnp file exists, if not, download from snp151Common table using mysql

if [ ! -f $FILE ]
then
mysql --user=genome --host=genome-mysql.cse.ucsc.edu -A -N -D hg38 -e 'SELECT chrom, chromStart, chromEnd, name FROM snp151Common' > snp151Common.bed
fi

#find positions of snps from the input list by comparing to snpdb
awk 'NR==FNR {h[$1] = 1; next} {if(h[$4]==1) print$0}' $SNPs $FILE > $1.bed
