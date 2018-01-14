import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Path to search files", required=True)
    parser.add_argument("-n", "--number", help="Number of files to look for (default=10)", 
            type=int, default=10)
    parser.add_argument("-f", "--fullpath", help="If true, use fullpath for filenames", 
            action="store_true", default=False)
    return parser.parse_args()
