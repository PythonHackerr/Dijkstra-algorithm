import argparse
import sys


def get_file_content(file_name):
    try:
        with open(file_name, 'r', encoding='utf8') as fh:
            arr = [[int(i) for i in line if i.isdigit()] for line in fh.readlines()]
            zeros = []
            for i, sub in enumerate(arr):
                for j, dig in enumerate(sub):
                    if dig == 0:
                        zeros.append((i, j))
            return arr, zeros
    except Exception:
        return []

def dijkstra():
    pass

def main():
    sys.setrecursionlimit(10000)
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    print(get_file_content(args.file)[1])

#command
#python main.py filename
if __name__ == "__main__":
    main()
