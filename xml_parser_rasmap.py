import xml.etree.ElementTree as ET
import os
import argparse
from gooey import Gooey, GooeyParser

master_rasmap_file = r'C:\python_projects\project_1\test_data\BRIGGSRN.rasmap'


@Gooey(program_name="Rasmap File Generator", default_size=(575, 600), advanced = True)
def parse_arguments():
    parser = GooeyParser(description = 'Rasmap File Creator')
    parser.add_argument('path',  help ='Paste the Models File Directory',widget='FileChooser')
    args = parser.parse_args()
    for models in os.listdir(args.path):
        models_path = os.path.join(args.path, models)
        rasmap_file = os.path.join(models_path , f'{models}.rasmap')
        with open(master_rasmap_file,encoding ='latin-1') as f:
            tree = ET.parse(f)
            root = tree.getroot()
            file_names = root.findall('Layer/Filename')
            for elem1 in root.iter('Layer'):
                filename = elem1.get('Filename')
                if filename == '.\BRIGGSRN.p01.hdf':
                    elem1.set('Filename', f'.\{models}.p01.hdf')
                elif filename == '.\BRIGGSRN.g01.hdf':
                    elem1.set('Filename', f'.\{models}.g01.hdf')
                else:
                    pass
        tree.write(rasmap_file)
    return


if __name__ == '__main__':
    parse_arguments()
