#-*- encoding: utf-8 -*-

import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())

    for i in xrange(N):
        tree_n = int(sys.stdin.readline().strip())
        TREE = []
        depth = 0
        print 'Case #%d:' % (i+1)
        for j in xrange(tree_n):
            line = sys.stdin.readline().strip()
            entry = line.replace('(', '').replace(')','').split()
            if entry != []:
                TREE.append((depth, entry))
            depth += line.count('(')
            depth -= line.count(')')

        animal_n = int(sys.stdin.readline().strip())
        animals = []
        for k in xrange(animal_n):
            arr = sys.stdin.readline().strip().split()
            animal_name = arr[0]
            features = arr[2:]

            P = 1.0
            skip = 0
            dest_depth = -1
            for depth, entry in TREE:
                if skip > 0:
                    if depth == dest_depth:
                        skip -= 1
                    if skip > 0:
                        continue
                P = P * float(entry[0])
                if len(entry) == 1:
                    break
                if not entry[1] in features:
                    skip = 2
                    dest_depth = depth+1
                else:
                    goto_next = False
            print '%8.7f' % P
