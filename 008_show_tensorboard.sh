#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Did you update the 'tensorflow_models' path in this script?"
read -rsp $'Press any key to continue...\n' -n 1 key
echo ">>>>>"
tensorboard --logdir="G:\Projects\tensorflow-windows-detector\model_output"
tensorboard --logdir="G:\Projects\tensorflow-windows-detector\eval"
# Output:
#