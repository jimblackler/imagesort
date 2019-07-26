import sys
import os
from PIL import Image
import filecmp

path = sys.argv[1]

for root, subdirs, files in os.walk(path):
    split_path = os.path.normpath(root).split(os.sep)
    if split_path[-1] in ['wide', 'tall']:
        use_root = os.sep.join(split_path[:-1])
    else:
        use_root = root

    for f in files:
        full = os.path.join(root, f)
        try:
            if not os.path.isfile(full):
                continue
            with Image.open(full) as image:
                if image.size[0] > image.size[1]:
                    use_dirname = 'wide'
                else:
                    use_dirname = 'tall'

            use_dir = os.path.join(use_root, use_dirname)

            if not os.path.exists(use_dir):
                os.mkdir(use_dir)
            new_location = os.path.join(use_dir, f)
            if full == new_location:
                continue
            if os.path.isfile(new_location):
                if filecmp.cmp(full, new_location):
                    print new_location + ' already exists - SAME FILE - deleting'
                    os.remove(full)
                else:
                    print new_location + ' already exists - DIFFERENT FILE'
                continue
            print full + ' -> ' + new_location
            os.rename(full, new_location)
        except IOError as e:
            print full
            print e