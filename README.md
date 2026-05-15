# CRAB Genomics Analysis Pipeline

A centralized repository compiling the computational, statistical, and automation workflows developed during genomic surveillance research at the Central Research Laboratory, KIMS. This workspace consolidates multi-language pipelines into structured modules to profile Carbapenem-Resistant *Acinetobacter baumannii* (CRAB) isolates.

## 🔬 Core Analytical Scope
The underlying research focuses on characterizing antimicrobial resistance (AMR) determinants, plasmid-associated mobility, and prophage-linked contexts in Indian isolates. It details the evolutionary dynamics of dominant lineages (e.g., ST2) carrying key carbapenemase genes (*blaOXA-23*, *blaNDM-1*, and *blaOXA-66*).

---

## 📁 Repository Structure & Technical Stack

### [ABA_notebooks](./ABA_notebooks)
*   **Purpose:** Jupyter notebooks serving as an execution record for the complete *Acinetobacter* genomics pipeline includes steps from installation to output generation.

### [CRAB_R_scripts](./CRAB_R_scripts)
*   **Purpose:** Modular R scripts for downstream processing, statistical filtering, contig-level annotations, and the generation of publication-ready figures.
*   **Structure:**
    *   `scripts/processing/`: Standardizes identifiers, parses multi-tool outputs, and creates unified data tables.
    *   `scripts/analysis/`: Quantifies flanking region profiles and gene–MGE (Mobile Genetic Element) associations.
    *   `scripts/visualization/`: Generates heatmaps and data visualizations using `ggplot2` and `pheatmap`.

### [phylogeny_processing](./phylogeny_processing)
*   **Purpose:** Dedicated python environment for core-genome phylogenetic processing.
*   **Tools:** Preprocessing workflow for tools like `Parsnp` and `clinker` for structural gene cluster comparisons and evolutionary interpretation.

### [Bioinformatics_tools](./Bioinformatics_tools)
*   **Purpose:** Jupyter workflow notebooks for Bioinformatics tools (installation to output generation)

---
**Author:** Nidhi Guntgatti  
**Affiliation:** Central Research Laboratory, KIMS
