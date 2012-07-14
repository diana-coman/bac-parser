#!/usr/bin/env python
from __future__ import print_function
import argparse
import cPickle
import functools
import logging
import logging.config
import sys

from utils import open_compressed_file

from bacparser.maintable import get_main_table_from_file
import bacparser.parsers

def get_data_from_file(f, year):
    parser = bacparser.parsers.get_parser(year)
    main_table = get_main_table_from_file(f, year)
    for i in parser.get_elev(main_table):
        yield i

def write_python(f, record):
    f.write(repr(record))
    f.write('\n#######################################################################\n')

def write_pickle(f, record):
    cPickle.dump(record, f, -1)

def parse_args():
    parser = argparse.ArgumentParser(
            description='Extract results from bacalaureat')
    parser.add_argument('--year', metavar='YEAR', type=int,
            choices=bacparser.parsers.SUPPORTED_YEARS,
            default=bacparser.parsers.SUPPORTED_YEARS[-1],
            help='Year of the exam')
    parser.add_argument('--format', metavar='FORMAT',
                        type=str, choices=('python', 'pickle'),
                        default='python')
    parser.add_argument('-o', '--output', metavar='OUTPUT',
                        type=lambda f: open(f, 'wb'), default=sys.stdout)
    parser.add_argument('filenames', metavar='FILE', type=str, nargs='+',
            help='Files to parse')
    return parser.parse_args()

def main():
    logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
    args = parse_args()
    if args.format == 'python':
        write = functools.partial(write_python, args.output)
    else: # 'pickle'
        write = functools.partial(write_pickle, args.output)
    with args.output:
        for filename in args.filenames:
            with open_compressed_file(filename) as f:
                logging.info("Extracting from %s" % (filename,))
                for i in get_data_from_file(f, args.year):
                    write(i)

if __name__ == '__main__':
    main()
