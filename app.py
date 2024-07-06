import fiftyone as fo
import fiftyone.brain as fob
import fiftyone.zoo as foz
from fiftyone import ViewField as F

# load dataset from the zoo
dataset = foz.load_zoo_dataset("coco-2017", split="validation")

# delete labels to simulate starting with unlabeled data
dataset.select_fields().keep_fields()

# # rename and persist to database
# dataset.name = "clustering-demo"
# dataset.persistent = True


res = fob.compute_visualization(
    dataset, 
    model="clip-vit-base32-torch", 
    embeddings="clip_embeddings", 
    method="umap", 
    brain_key="clip_vis", 
    batch_size=10
)
dataset.set_values("clip_umap", res.current_points)


# launch the app to visualize the dataset
session = fo.launch_app(dataset)
