#!/usr/bin/env python

import argparse
import logging
import time


logging.basicConfig(format='%(asctime)s	%(levelname)s	%(message)s',
                    datefmt='%Y%m%d %H:%M',
                    level=logging.INFO)


def cookie_clicker(in_file, out_file):

    with open(in_file, 'r') as fin:
        with open(out_file, 'w') as fout:
            n_case = int(fin.readline().strip())

            for i_case in range(n_case):
                T = 0.0
                R = 2.0
                C, F, X = [float(x) for x in fin.readline().strip().split(' ')]

                t1 = X / R
                t2 = C / R + X / (R + F)
                while t1 >= t2:
                    T += C / R      # wait until saving C
                    R += F          # buying a farm

                    # update estimated time
                    t1 = X / R
                    t2 = C / R + X / (R + F)
                
                # no need to buy a farm
                T += t1

                fout.write('Case #{}: {:.7f}\n'.format(i_case + 1, T))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', '-i', required=True, dest='infile')
    parser.add_argument('--output-file', '-o', required=True, dest='outfile')
    args = parser.parse_args()

    start = time.time()
    cookie_clicker(in_file=args.infile,
                 out_file=args.outfile)

    logging.debug('finished ({:.2f} min elasped).'.format((time.time() - 
                                                           start) / 60.))
