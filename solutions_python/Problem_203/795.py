#!/usr/bin/env python3

import numpy as np



def main():
    tests = int(input())
    
    for case in range(1, tests+1):
        r, c = [int(word) for word in input().split()]
        cake = []
        for _ in range(r):
            cake.append(input())
            
        cake = np.array([[col for col in row] for row in cake])
        
        def solve(cake):
            for size in range(r*c, 0, -1):
                if '?' not in np.unique(cake):
                    break
            
                for x in range(1, c+1):
                    if size % x != 0:
                        continue
                        
                    y = size // x

                    if y > r:
                        continue
                                        
                    for i in range(r-y+1):
                        for j in range(c-x+1):
                            slice = cake[i:i+y,j:j+x]
                            
                            unique = np.unique(slice)
                            
                            if '?' not in unique:
                                continue
                            
                            if len(unique) != 2:
                                continue
                                
                            initial = unique[0] if unique[0] != '?' else unique[1]
                            
                            mask = np.ones(cake.shape, np.bool)
                            mask[i:i+y,j:j+x] = 0
                            
                            if np.any(cake[mask] == initial):
                                continue
                            
                            cake[i:i+y,j:j+x] = initial
                            
            return cake
        
        try:
            cake = solve(cake.copy())
        except:
            print(cake)
            raise
        
        print('Case #{}:'.format(case))
        for line in cake:
            print(''.join(line))


if __name__ == '__main__':
    main()