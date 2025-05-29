# Complete UCSC to RefSeq chromosome mapping for GRCm38 (mm10)
chr_map = {
    "chr1": "NC_000067.6",
    "chr2": "NC_000068.7",
    "chr3": "NC_000069.6",
    "chr4": "NC_000070.6",
    "chr5": "NC_000071.6",
    "chr6": "NC_000072.6",
    "chr7": "NC_000073.6",
    "chr8": "NC_000074.6",
    "chr9": "NC_000075.6",
    "chr10": "NC_000076.6",
    "chr11": "NC_000077.6",
    "chr12": "NC_000078.6",
    "chr13": "NC_000079.6",
    "chr14": "NC_000080.6",
    "chr15": "NC_000081.6",
    "chr16": "NC_000082.6",
    "chr17": "NC_000083.6",
    "chr18": "NC_000084.6",
    "chr19": "NC_000085.6",
    "chrX": "NC_000086.7",
    "chrY": "NC_000087.7",
    "chrM": "NC_005089.1",
    "chrUn_GL456210.1": "NT_166280.1",
    "chrUn_GL456211.1": "NT_166281.1",
    "chrUn_GL456212.1": "NT_166282.1",
    "chrUn_GL456213.1": "NT_166283.1",
    "chrUn_GL456221.1": "NT_166291.1",
    "chrUn_GL456354.1": "NT_187052.1",
    "chrUn_GL456359.1": "NT_166434.1",
    "chrUn_GL456360.1": "NT_187053.1",
    "chrUn_GL456366.1": "NT_187054.1",
    "chrUn_GL456367.1": "NT_187055.1",
    "chrUn_GL456368.1": "NT_187056.1",
    "chrUn_GL456370.1": "NT_187057.1",
    "chrUn_GL456372.1": "NT_187058.1",
    "chrUn_GL456379.1": "NT_166438.1",
    "chrUn_GL456381.1": "NT_187059.1",
    "chrUn_JH584292.1": "NT_165789.2",
}

input_gtf = "mm10.gtf.old"      # Your original GTF file
output_gtf = "mm10.gtf"         # Output GTF file with RefSeq-style chr names

with open(input_gtf, 'r') as infile, open(output_gtf, 'w') as outfile:
    for line in infile:
        if line.startswith("#"):
            outfile.write(line)
            continue
        parts = line.strip().split('\t')
        chrom = parts[0]
        if chrom in chr_map:
            parts[0] = chr_map[chrom]
        outfile.write('\t'.join(parts) + '\n')

print(f"Conversion complete. Output written to: {output_gtf}")
