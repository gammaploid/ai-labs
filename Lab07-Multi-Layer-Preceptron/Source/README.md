
# File: README.md
# Description: Instructions for running the source code for Lab 7.
# Licence: MIT Licence

## Description
This directory contains the source code for Lab 7, which focuses on Multi-Layer Perceptrons (MLPs) for time series forecasting. The main file is a Jupyter Notebook `Lab07.ipynb` that covers:
- Building and training MLPs using scikit-learn on the sunspot dataset.
- Evaluating the effect of hidden layers, node counts, and activation functions.
- Performing hyperparameter optimization using Grid Search.
- Implementing and comparing MLP models in PyTorch and MLX.
- Visualizing neural network architectures with `visualtorch`.

## Requirements
All required Python packages are listed in `requirements.txt`. To install them, run the following command in your terminal:
```bash
pip install -r requirements.txt
```

## How to Run
1.  Ensure you have installed the required packages from `requirements.txt`.
2.  Open the Jupyter Notebook `Lab07.ipynb` in a compatible environment (like VS Code, Jupyter Lab, or Jupyter Notebook).
3.  Run the cells in the notebook sequentially to see the analysis and results.

## Known Bugs or Limitations
- The `mlx` package is only available on Apple Silicon hardware. The notebook will fall back gracefully if it is not available.
- There are no other known bugs at this time.