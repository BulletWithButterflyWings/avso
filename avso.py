import argparse, os,csv
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f",type=str ,help="increase output file verbosity")
args = parser.parse_args()
print(args.file)
with open(args.file, newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
        #print(row['first_name'], row['last_name'])
        print(row)