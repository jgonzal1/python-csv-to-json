"""
module that transforms a CSV to JSON
"""
import csv
import json
import sys
from collections import defaultdict

'''
main function which takes 2 col length CSVs
'''
def transform(argv):
  csvfile = open(argv[0],'r')
  fichJSON = open(argv[1],'w')
  
  fieldnames = ("Col1", "Col2")
  reader = csv.DictReader(csvfile, fieldnames) # assigned the json keys with fieldnames

  output = []
  for each in reader:
      row = {}
      for field in fieldnames:
          row[field] = each[field]
      output.append(row)       
  json.dump(output, fichJSON, indent=3, sort_keys=True)
  regroup = defaultdict(list)

if __name__ == '__main__':
    transform(sys.argv[1:])

