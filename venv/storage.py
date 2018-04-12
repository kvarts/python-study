import os
import tempfile
import argparse

delimiter = ":"

storage_path = os.path.join(tempfile.gettempdir(), 'storage3.data')

def write_value(key, value):
    with open(storage_path, "a+") as f:
        f.write(key + delimiter + value + "\n")

def read_value(key):
    values = []
    if not os.path.isfile(storage_path):
        return values

    with open(storage_path, 'r') as f:
        for line in f:
            [line_key, line_value] = line.split(delimiter)
            if line_key == key:
                values.append(line_value.strip())
    return values

def print_values(values):
    if not values:
        print(None)
    else:
         print(', '.join(values))


parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
if not args.val:
    print_values(read_value(args.key))
else:
    write_value(args.key, args.val)