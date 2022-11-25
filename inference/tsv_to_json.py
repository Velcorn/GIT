import csv
import json

# Path to TSV file
path = 'GIT_LARGE_TextVQA/'

# Open the TSV and convert to list of dictionaries
with open(f'{path}/vizwiz.tsv') as f:
    dict_list = [{'image': f'VizWiz_test_{dict(json.loads(line[0]))["question_id"].zfill(8)}.jpg', 'answer': dict(json.loads(line[0]))['answer']} for line in csv.reader(f, delimiter='\t')]

# Save to JSON
with open(f'{path}/test_predict_git_textvqa.json', 'w') as f:
    json.dump(dict_list, f)
