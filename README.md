# Jupyter Notebook Cells Classification

The data scientists’ workflow is consisted of data gathering, data exploration, data preparation and cleaning, feature engineering, training a model and tuning its parameters, evaluating the model etc. until they achieve the business goals and the model is deployed.

We gathered a dataset of ~95k Jupyter notebook cells from Kaggle.

Our task is to classify those cells into the relevant Data-Science workflow stage.
To do so we first used weak supervision using Snorkel (as our data is unlabeled), then we created an LSTM model.

For more detailed explanations and results see the [documentation](https://github.com/tamirhuber/Jupyter-Notebook-Cells-Classification/blob/master/Documentation.pdf).

The first notebook is "Exploration_and_WeakSupervision.ipynb" and as the name implies it contains our data exploration and tagging using snorkel weak supervision. It will automatically open the second notebook, that contains our end-classification-model (LSTM).

*If you are only intrested in the end-model you may start with the second notebook "Classification.ipynb"*

**Note** - snorkel.db, LSTM.h5 and the checkpoints folder enable you to load already existing database and trained model and skip long executions. Follow the instructions in the notebooks. 

_Developers: Yoav Shechter, Omer Edelstein, Gur Yaniv, Tamir Huber_
