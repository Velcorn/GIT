"""
Adapt the prepare_coco_test() function to work for the VizWiz dataset.
The format of the TSV files is:
image_tsv: image-id, image as base64 encoded string
question_tsv: image-id, question text (lowercase)

Author: Jan Willruth
"""

import base64
import os.path as op
import json
from generativeimage2text.common import json_dump, read_to_buffer
from generativeimage2text.tsv_io import tsv_writer


def main():
    print('Converting dataset to TSV files...')
    subset = 'test'
    image_folder = f'vizwiz/{subset}'
    json_file = f'vizwiz/Annotations/{subset}.json'
    infos = json.loads(read_to_buffer(json_file))

    def gen_img_rows():
        for info in infos:
            name = info['image']
            payload = base64.b64encode(read_to_buffer(op.join(image_folder, name)))
            yield name, payload
    tsv_writer(gen_img_rows(), f'vizwiz/image_{subset}.tsv')

    def gen_question_rows():
        for info in infos:
            name = info['image']
            question = [{'question_id': name, 'question': info['question'].lower()}]
            yield name, json_dump(question)
    tsv_writer(gen_question_rows(), f'vizwiz/question_{subset}.tsv')

    return 'Finished creating tsv files!'


if __name__ == '__main__':
    print(main())
    print('All done!')
