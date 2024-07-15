## Clustering-with-FiftyOne
This project demonstrates how to structure unstructured visual data using clustering techniques with FiftyOne and Scikit-learn. We use CLIP embeddings and UMAP for dimensionality reduction and visualize clusters with the FiftyOne App. Additionally, we label clusters using GPT-4V to enhance understanding of cluster characteristics.

## Overview
This repository contains the code and resources for clustering visual data using deep learning models and popular clustering algorithms. The goal is to provide insights into data patterns and inherent structures.

## Dataset
The example uses the validation split (5,000 samples) from the MS COCO dataset. However, you can use your own dataset by modifying the data loading section in app.py.

## Project Structure
- `data/:` Contains the dataset.
- `src/:` Source code for the project, including data processing and clustering scripts.
- `results/:` Evaluation results and performance metrics.
- `app.py:` Main application script.

## Installation
1. To run this project, you need Python 3.7+ and the following dependencies:

```bash
pip install -U scikit-learn fiftyone umap-learn
pip install git+https://github.com/openai/CLIP.git
```
2. Install the FiftyOne Clustering Plugin:

```bash
fiftyone plugins download https://github.com/jacobmarks/clustering-plugin
```
3. Set up the OpenAI API key for GPT-4V:

```bash
export OPENAI_API_KEY=sk-...
```
## Usage
1. Clone the repository:
```bash
git clone https://github.com/yugeshsivakumar/Clustering-with-FiftyOne.git
cd Clustering-with-FiftyOne
```
2. Run the app.py script to load data, create features, compute clusters, and visualize them:

```bash
python app.py
```

3. The FiftyOne App will launch automatically. If running in a Jupyter Notebook, pass auto=False to fo.launch_app() and open the URL manually (typically http://localhost:5151/).

4. Use the FiftyOne Clustering Plugin to compute and visualize clusters:

- Press the backtick key (`) in the FiftyOne App.
- Type compute_clusters and select it from the dropdown.
- Choose clustering method (kmeans or HDBSCAN), feature vectors (clip_umap), and other parameters.
- Visualize clusters and embeddings in the app.
5. Label clusters using GPT-4V:

- Ensure your OpenAI API key is set.
- Use the label_clusters_with_gpt4v operator in the FiftyOne App to label clusters.

## Results
After running app.py, navigate to http://localhost:5151/ to access the application. Visualize your clusters in the FiftyOne App and explore the structure of your data. The labeling with GPT-4V provides meaningful insights into cluster characteristics.




![result](https://github.com/yugeshsivakumar/Testing_Repo/assets/156910899/e92874b4-0a20-4e65-9c43-616bba110939)




## Acknowledgements
- The creators and maintainers of the FiftyOne and Scikit-learn libraries.
- OpenAI for providing the CLIP model and GPT-4V.
- The open-source community for continuous support and contributions.

