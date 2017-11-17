import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

# source and credits:
# https://raw.githubusercontent.com/datitran/raccoon_dataset/master/xml_to_csv.py

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def train():
    image_path = os.path.join(os.getcwd(), 'data', 'tf_windows_train', 'annotations','xmls')
    xml_df = xml_to_csv(image_path)
    labels_path = os.path.join(os.getcwd(), 'data', 'tf_windows_train','train.csv')
    xml_df.to_csv(labels_path, index=None)
    print('> tf_windows_train - Successfully converted xml to csv.')

def val():
    image_path = os.path.join(os.getcwd(), 'data', 'tf_windows_val', 'annotations','xmls')
    xml_df = xml_to_csv(image_path)
    labels_path = os.path.join(os.getcwd(), 'data', 'tf_windows_val', 'val.csv')
    xml_df.to_csv(labels_path, index=None)
    print('> tf_windows_val -  Successfully converted xml to csv.')

train()
val()
#run ok by sanghv