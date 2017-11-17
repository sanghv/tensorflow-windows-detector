#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

python 004_generate_tfrecord.py --images_path=data/tf_windows_train/images --csv_input=data/tf_windows_train/train.csv  --output_path=data/train.record
python 004_generate_tfrecord.py --images_path=data/tf_windows_val/images --csv_input=data/tf_windows_val/val.csv  --output_path=data/val.record
