#!/usr/bin/env python

"""Google Code Jam 2010, Round 1B."""

import sys

def read_from(fh, num):
    return [fh.readline().rstrip() for i in xrange(num)]

def update(D, p):
    if p == "" or D.has_key(p):
        return 0
    else:
        parent_cost = update(D,p[0:p.rindex("/")])
        D[p] = 1
        return 1 + parent_cost

def path_cmp(x, y):
    return x.count("/") - y.count("/")

def calc_res(e_paths, n_paths):
    #use a hash with each dir (and all of its parent paths) as keys.
    D = {}
    for e in e_paths:
        update(D, e)
    #order the new paths be number of components (smallest to largest) first
    #to ensure we limit the number of new paths that need to be created
    n_paths.sort(path_cmp)
    count = 0
    for n in n_paths:
        count += update(D, n)
    return count

def main(args):
    if len(args) < 2:
        return 1
    try:
        f = open(args[1])
        #READ appropriate args from initial lines
        num_cases = int(f.readline())
        for case in xrange(num_cases):
            #READ appropriate args for this case
            M,N = [int(x) for x in f.readline().split()]
            existing_list = read_from(f, M)
            new_list = read_from(f, N)
            #CALCULATE answer for this case
            print "Case #" + str(case+1) + ": " + str(calc_res(existing_list,
                  new_list))
    except IOError:
        print "Invalid file input"
        return 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))
