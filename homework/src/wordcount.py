# Ejemplo para casos de uso
# python3 -m homework data/input data output

import sys


def parse_args():
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    return input_folder, output_folder


def main():
    args = parse_args()
