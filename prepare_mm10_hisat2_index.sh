#!/bin/bash

GENOME_DIR="reference"
HISAT2_INDEX_DIR="${GENOME_DIR}/mm10_hisat2_index"
GENOME_FASTA="${GENOME_DIR}/mm10.fa"
GTF_FILE="${GENOME_DIR}/mm10.gtf"

mkdir -p $GENOME_DIR
mkdir -p $HISAT2_INDEX_DIR

# Download the mm10 genome (FASTA) and GTF annotation file (grcm38 == mm10)
printf "Downloading mm10 genome FASTA...\n"
curl -L -o $GENOME_FASTA.gz ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/635/GCF_000001635.26_GRCm38.p6/GCF_000001635.26_GRCm38.p6_genomic.fna.gz
printf "Downloading mm10 genome GTF annotation...\n"
curl -L -o $GTF_FILE.gz ftp://ftp.ensembl.org/pub/release-102/gtf/mus_musculus/Mus_musculus.GRCm38.102.gtf.gz

printf "Unzipping mm10 genome...\n"
gunzip $GENOME_FASTA.gz
printf "Unzipping mm10 GTF...\n"
gunzip $GTF_FILE.gz

# Build HISAT2 index
printf "Building HISAT2 index...\n"
hisat2-build $GENOME_FASTA $HISAT2_INDEX_DIR/mm10

printf "mm10 HISAT2 index is ready at: $HISAT2_INDEX_DIR\n"
