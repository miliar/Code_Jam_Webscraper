'''
@author: csalazar
'''
#!/usr/bin/env python3
import sys
import itertools

import collections

if __name__ == "__main__":
    f = sys.stdin
    n_tests = int(f.readline())
    
    for i in range(1, n_tests+1):
        line = [int(x) for x in f.readline().split(' ')]
        n_numbers = line[0]
        numbers = line[1:]
        superset = {}
        flag = False

        for j in range(1, n_numbers+1):
            set_i = list(itertools.combinations(numbers, j))

            for s in set_i:
                if s not in superset.keys():
                    s_sum = sum(s)
                    if s_sum in superset.values():
                        print('Case #%d:' % i)
                        print(' '.join([str(n) for n in s]))
                        
                        for name, value in superset.items():
                            if value == sum(s):
                                print(' '.join([str(n) for n in name]))
                                break
                        flag = True
                        break
                    superset[s] = s_sum
            if flag:
                break
        
        if not flag:
            print('Case #%d:' % i)
            print('Impossible')