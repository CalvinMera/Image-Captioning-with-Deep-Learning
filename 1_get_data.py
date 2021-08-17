import tensorflow as tf # Used to download a file from a URL: tf.keras.utils.get_file().
import os # Used to handle pathnames.

# First, we download the annotation files.

annotation_folder = '/data/annotations/'

# We store all of the data in /Users/calvin/projects/mlp_1/data.
# Given some zipped file, file.zip when one unzips it a folder is created, which houses the contents of file.zip.
# This folder inherits its name from the zipped file, namely, file.

if not os.path.exists(os.path.abspath('.') + annotation_folder):

    # First, we generate the current working directory with os.path.abspath('.').
    # Note that the directory should be set to whenever get_data.py lives.
    # Then, we concatenate that path with the path to the data.
    # Lastly, we use os.path.exists() to check if the folder exists, which it does not.
    # Thanks to the not operator, the if block statement is executed.

    annotation_zip = tf.keras.utils.get_file('annotations.zip',
                                          cache_subdir=os.path.abspath('.') + '/data',
                                          origin = 'https://ivc.ischool.utexas.edu/VizWiz_final/caption/annotations.zip',
                                          extract = True)
    
    # The first input is what we will name the downloaded file.
    # The second input is where the downloaded file will be saved.
    # The third input is the URL where the file lives.
    # Lastly, the fourth input unzips the downloaded file.

    # Incase we need the pathnames to the training, validation, and testing annotation data sets we downloaded, we
    # save them below. We use os.path.dirname to extract the directory that the zipped file was extracted to and then
    # concatenate the rest of the filepath that leads us to the file of interest.
    # Note we could have used os.path.abspath('.'), but we would have had to perform the following replacement:
    # '/annotations/train.json' -> '/data/annotations/train.json'

    # annotation_train = os.path.dirname(annotation_zip)+'/annotations/train.json'
    # annotation_val = os.path.dirname(annotation_zip)+'/annotations/val.json'  
    # annotation_test = os.path.dirname(annotation_zip)+'/annotations/test.json'

    os.remove(annotation_zip) # We remove the filepath.

# Unlike the annotations.zip file that stored together the training, validation, and testing annotation data, the
# image data is stored in 3 different files, which each need to be uncompressed individually.

image_folders = ['/data/images/val/','/data/images/test/','/data/images/train/']
names_and_endings = ['val.zip','test.zip','train.zip']
altogether = zip(image_folders, names_and_endings)

for image_folder, name_and_ending in altogether:
    if not os.path.exists(os.path.abspath('.') + image_folder):
        image_zip = tf.keras.utils.get_file(name_and_ending,
        cache_subdir = os.path.abspath('.') + '/data/images',
        origin = 'https://ivc.ischool.utexas.edu/VizWiz_final/images/' + name_and_ending,
        extract = True)

        # PATH = os.path.dirname(image_zip) + image_folder
        # Why save the path if it is going to be overwritten?
        os.remove(image_zip)
    # else:
    #     PATH = os.path.abspath('.') + image_folder