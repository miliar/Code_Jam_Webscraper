#!/usr/bin/env python

import argparse
import logging
import time


logging.basicConfig(format='%(asctime)s	%(levelname)s	%(message)s',
                    datefmt='%Y%m%d %H:%M',
                    level=logging.INFO)


def magic_trick(in_file, out_file):

    with open(in_file, 'r') as fin:
        with open(out_file, 'w') as fout:
            n_case = int(fin.readline().strip())

            for i_case in range(n_case):
                ans1 = int(fin.readline().strip())
                for i_row in range(4):
                    row = fin.readline()
                    if i_row + 1 == ans1:
                        row1 = set(row.strip().split(' '))

                ans2 = int(fin.readline().strip())
                for i_row in range(4):
                    row = fin.readline()
                    if i_row + 1 == ans2:
                        row2 = set(row.strip().split(' '))

                sols = row1.intersection(row2)
                n_sol = len(sols)
                if n_sol == 1:
                    fout.write('Case #{}: {}\n'.format(i_case + 1,
                                                       list(sols)[0]))
                elif n_sol > 1:
                    fout.write('Case #{}: Bad magician!\n'.format(i_case + 1))
                else:
                    fout.write('Case #{}: Volunteer cheated!\n'.format(i_case + 1))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', '-i', required=True, dest='infile')
    parser.add_argument('--output-file', '-o', required=True, dest='outfile')
    args = parser.parse_args()

    start = time.time()
    magic_trick(in_file=args.infile,
                 out_file=args.outfile)

    logging.debug('finished ({:.2f} min elasped).'.format((time.time() - 
                                                           start) / 60.))
