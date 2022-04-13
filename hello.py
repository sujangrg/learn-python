#!/usr/bin/env python

import argparse
from email import parser

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')

args = parser.parse_args()

print('Hello, ' + args.name + '!')

