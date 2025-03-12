# RNA-Seq Pipeline with for mm10 (hisat2 + featureCounts)


## Overview

This pipeline processes RNA-seq data using the following steps:

- Quality filtering with FastP.
- Alignment of clean reads to the mm10 genome using HISAT2.
- Gene expression quantification with FeatureCounts.

## Prerequisites

- Python 3.9
- Conda (for managing dependencies)
- Snakemake (for workflow execution)

## Getting Started


### Step 1: Setting up the Environment


1. Clone or download this repository.

1. Create the Conda environment using the `environment.yml` file: `conda env create -f workflow/envs/environment.yml`

1. Activate the environment:  `conda activate rnaseq_pipeline`


### Step 2: Prepare mm10 Reference Files


1. Run the script to download and prepare the mm10 reference files: `./prepare_mm10_hisat2_index.sh`


##### This will: 
- Download the mm10 genome (FASTA) and GTF file from Ensembl.
- Build the HISAT2 index in the reference/mm10_hisat2_index/ directory.

### Step 3: Prepare Your Input Data
- Place your raw FASTQ files in the `raw_data/` folder. The files should be named as:
    ```
    {sample}.fastq.gz
    ```
    Where `{sample}` is your sample name.

### Step 4: Configure the Workflow

- Edit the `workflow/config.yaml` file to list the sample names and reference paths:
```yaml 
samples:
  - sample1
  - sample2
  - sample3

reference:
  mm10_hisat2: "reference/mm10_hisat2_index"
  mm10_gtf: "reference/mm10.gtf"
```

### Step 5: Running the Pipeline
1. Run Snakemake to start the workflow: `snakemake --use-conda --cores <number of cores>`
    - *Note: consider using tmux/screen/etc. as this may take a while and may be stopped on loss of connection if working on a remote machine.*
1. Results:
    - All tool outputs can be found in `results/` folder.

## Pipeline Steps

### Read Filtering:
- Tool: FastP
    - Parameters: Removes low-quality reads, trims adapters, and outputs cleaned reads in FASTQ format.

### Genome Alignment:
- Tool: HISAT2
    - Parameters: Aligns cleaned reads to the mm10 genome.

### Gene Expression Quantification:
- Tool: FeatureCounts
    - Parameters: Quantifies gene expression based on aligned BAM files and the mm10 GTF annotation.

## License 
This pipeline is open source and available under the **MIT license**.
