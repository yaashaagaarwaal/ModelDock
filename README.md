# MLOps Workbench

A practical environment for understanding the fundamentals of reproducible machine learning workflows.

## Overview

This project demonstrates a few foundational MLOps practices that help make machine learning experiments reliable, repeatable, and easier to reproduce across different environments.

The workflow focuses on:

* Managing an isolated Python environment
* Identifying the Python interpreter used by a project
* Tracking installed library versions
* Creating pinned dependency files
* Controlling randomness with deterministic seeds
* Generating reproducible datasets
* Creating file fingerprints for experiment tracking
* Recording work with Git

## Why Reproducibility Matters

Machine learning experiments can produce different results when they are executed in different environments or at different times.

Differences in:

* Python versions
* Library versions
* Random seeds
* Dependencies
* Input data

can affect the final output.

A reproducible workflow helps ensure that the same code, data, environment, and configuration can consistently produce the same result.

## Project Structure

```text
P01-workbench/
│
├── P01.ipynb
├── work/
│   └── my_requirements.txt
└── README.md
```

## Key Concepts

### 1. Virtual Environment

The project uses an isolated Python environment so that its dependencies remain independent from other projects.

This helps avoid dependency conflicts and makes the development environment easier to reproduce.

### 2. Dependency Pinning

Required libraries are recorded with their exact versions.

Example:

```text
numpy==2.5.1
```

Pinning dependencies makes it possible to recreate an environment with the same library versions.

### 3. Random Seeds

Machine learning workflows frequently use random number generation.

Without a fixed seed, repeated executions can produce different results.

For example:

```python
import numpy as np

rng = np.random.default_rng(42)
```

Using a fixed seed makes the generated results deterministic.

### 4. Reproducible Dataset Generation

The workflow generates a dataset using a controlled random generator and verifies that repeated executions produce consistent results.

This provides a simple demonstration of deterministic experimentation.

### 5. File Fingerprinting

A fingerprint can be generated from a file to uniquely represent its contents.

A common approach is to use a cryptographic hash such as SHA-256:

```python
import hashlib

def fingerprint(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
```

If the file contents change, its fingerprint also changes.

This can be useful for tracking datasets and experiment artifacts.

### 6. Git Version Control

Git is used to record the project history and provide a reproducible record of changes.

A typical workflow is:

```bash
git status
git add .
git commit -m "Initialize MLOps workbench"
```

## Workflow

The notebook follows this sequence:

1. Identify the active Python interpreter
2. Inspect the installed environment
3. Record dependency versions
4. Create a pinned requirements file
5. Demonstrate uncontrolled randomness
6. Introduce deterministic random seeds
7. Generate reproducible data
8. Inspect the generated dataset
9. Generate a file fingerprint
10. Record the project state with Git

## Requirements

The project is designed to run inside a Python virtual environment.

Install the required dependencies using:

```bash
pip install -r work/my_requirements.txt
```

## Running the Notebook

Start Jupyter from the project environment:

```bash
jupyter notebook
```

Then open:

```text
P01.ipynb
```

Run the notebook from top to bottom so that all outputs are generated in sequence.

## Reproducibility

The project follows the basic reproducibility principle:

```text
Same Code
   +
Same Data
   +
Same Dependencies
   +
Same Configuration
   ↓
Reproducible Result
```

This forms the foundation for more advanced MLOps practices such as experiment tracking, model versioning, automated pipelines, and deployment.

## Learning Outcomes

After completing this project, you should understand:

* Why isolated environments are useful
* Why dependency versions should be pinned
* How random seeds affect machine learning experiments
* How deterministic data generation works
* How file hashes can identify artifacts
* How Git contributes to reproducible workflows

## References

* Python Virtual Environments
* pip Requirements Files
* NumPy Random Number Generation
* Git Version Control
