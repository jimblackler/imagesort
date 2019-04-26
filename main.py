import sys
import os
from PIL import Image

path = sys.argv[1]

for root, subdirs, files in os.walk(path):
    split_path = os.path.normpath(root).split(os.sep)
    if split_path[-1] in ['wide', 'tall']:
        continue
    for f in files:
        full = os.path.join(root, f)
        try:
            if os.path.isfile(full):
                with Image.open(full) as image:
                    if image.size[0] > image.size[1]:
                        use_dirname = 'wide'
                    else:
                        use_dirname = 'tall'

                use_dir = os.path.join(root, use_dirname)

                if not os.path.exists(use_dir):
                    os.mkdir(use_dir)
                new_location = os.path.join(use_dir, f)
                print full + ' -> ' + new_location
                os.rename(full, new_location)
        except IOError as e:
            print e