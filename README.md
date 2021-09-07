# Image-Captioning-with-Deep-Learning
We adapted and heavily annotated (for pedagogical reasons) the TensorFlow tutorial on image captioning.

See https://www.tensorflow.org/tutorials/text/image_captioning.

We hope that others find the numerous comments and print statements as helpful and insightful as we did.

Below we briefly describe what was done.

1. We studied the VizWiz-Captions image dataset instead of the image dataset that was featured in the tutorial. We picked this dataset in order to appreciate the impact a dataset can have on powerful deep learning models. The dataset was downloaded by running 1_get_data.py.
2. The training and validation datasets were preprocessed with the help of pandas in 2_preprocessing_train_val.ipynb. There are several choices that must be made, such as deciding the minimum number of captions an image should have if it is to partcipate in the dataset and whether or not to impose a cutoff on the size of the captions.
3. Further data preprocessing, such as tokenizing/padding captions and manipulating images so that their tensorial representation is in alignment with the requirements of the ResNet-50 model was carried out in 3_preprocess_model_train_evaluate.ipynb. After the end of the preprocessing era, we proceeded to create an Encoder-Decoder model with ResNet-50 at one end, and gated recurrent units armed with Bahdanau attention at the other end. The notebook ends with training and evaluation.

There is still much more work to be done!
