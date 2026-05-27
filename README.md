# AI-Powered Variant Prioritization Tool for Rare Genetic Diseases



**Author:** Amruta Subhash Rawool

**Tech Stack:** Python, PyTorch, XGBoost, Flask, Docker, HPO API

## 🧬 Project Overview

Identifying the specific genetic variants responsible for a patient's rare disease is a critical "needle in a haystack" problem. Whole Exome Sequencing (WES) typically yields **~20,000 variants** per patient, leading to analysis paralysis for clinicians.

This project provides an end-to-end AI pipeline that ingests a patient **VCF file** and clinical **HPO symptom terms** to return a ranked shortlist of the **Top 20** most likely causal variants with interpretable evidence scores.

### Key Impact

* **Reduces Manual Curation:** Automates tasks that previously took days or weeks.


* **Unified Evidence View:** Consolidates data from ClinVar, gnomAD, OMIM, and Ensembl.


* **Interpretable AI:** Uses SHAP values to explain why specific variants were prioritized.



## 🛠 System Architecture

The tool follows a 6-stage pipeline to transform raw genomic data into clinical insights:

1. **Input Layer:** Supports GRCh37/38 VCF uploads and HPO symptom terms.


2. **Annotation Engine:** Parallel queries to live databases for pathogenicity and frequency.


3. **HPO Integration:** Calculates semantic similarity between patient symptoms and disease phenotypes.


4. **Feature Matrix:** Assembles a 45-feature vector across 9 distinct domains.


5. **ML Classifier:** An ensemble of XGBoost and a PyTorch Deep Learning MLP.


6. **Ranked Output:** Returns Top-N variants with pathogenicity tiers and evidence cards.



## 📊 Feature Engineering (9 Domains)

The classifier evaluates every variant based on the following feature sets:

| # | Domain | Key Features |
| --- | --- | --- |
| 1 | **Population Frequency** | gnomAD global and population-specific allele frequencies

 |
| 2 | **Pathogenicity Scores** | ClinVar labels and review status

 |
| 3 | **Functional Impact** | SIFT, PolyPhen-2, and consequence terms

 |
| 4 | **Conservation** | CADD PHRED, PhyloP100, and GERP++

 |
| 5 | **Protein Structure** | UniProt domain hits and PTM overlaps

 |
| 6 | **HPO Phenotype Sim.** | Resnik Information Content (IC) similarity scores

 |
| 7 | **Inheritance Pattern** | OMIM-based AD/AR/XL modes and de novo flags

 |
| 8 | **Gene Constraint** | gnomAD pLI, LOEUF, and Z-scores

 |
| 9 | **Literature Evidence** | PubMed and HGMD variant mention counts

 |

## 📈 Performance Metrics

* **AUROC:** 0.92 on ClinVar hold-out sets.


* **Recall@20:** 85% (Causal variant found in top 20 results).


* **Mean Reciprocal Rank (MRR):** ≥ 0.70.


* **Latency:** < 90 seconds from upload to ranked output.



## 🚀 Deployment & Usage

This application is containerized with **Docker** for easy deployment to cloud platforms like AWS, GCP, or Render.

### Local Setup

1. Clone the repository.
2. Build the image: `docker build -t variant-tool .`
3. Run the container: `docker run -p 5000:5000 variant-tool`
4. Open `localhost:5000` in your browser.


## 🔮 Future Work

* **Trio Analysis:** Adding de novo variant detection using parent-child VCF trios.


* **RNA-seq Integration:** Incorporating splicing impact scores (SpliceAI).


* **Clinical NLP:** Automatically extracting HPO terms from unstructured clinical notes using BioBERT.

