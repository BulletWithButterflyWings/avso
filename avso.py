import argparse, os
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f",type=str ,help="increase output file verbosity")
args = parser.parse_args()
print(args.file)