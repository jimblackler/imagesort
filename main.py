import sys
import os
from PIL import Image

path = sys.argv[1]

for f in os.listdir(path):
    full = os.path.join(path, f)
    wide_dir = os.path.join(path, 'wide')
    tall_dir = os.path.join(path, 'tall')

    if os.path.isfile(full):
        with Image.open(full) as image:
            if image.size[0] > image.size[1]:
                use_dir = wide_dir
            else:
                use_dir = tall_dir

        if not os.path.exists(use_dir):
            os.mkdir(use_dir)
        new_location = os.path.join(use_dir, f)
        os.rename(full, new_location)