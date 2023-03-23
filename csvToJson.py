"""
Module that transforms a CSV to JSON
"""
import csv
import json
import sys
from collections import defaultdict

'''
Main function which takes 2 col length CSVs
'''
def transform(argv):
  csv_file_input = open(argv[0], 'r')
  json_file_output = open(argv[1], 'w')
  
  column_key_names = ("Col1", "Col2")
  reader = csv.DictReader(csv_file_input, column_key_names) # assigned the json keys with fieldnames

  output = []
  for each in reader:
      row = {}
      for field in column_key_names:
          row[field] = each[field]
      output.append(row)       
  json.dump(output, json_file_output, indent=3, sort_keys=True)
  regroup = defaultdict(list)

if __name__ == '__main__':
    transform(sys.argv[1:])

