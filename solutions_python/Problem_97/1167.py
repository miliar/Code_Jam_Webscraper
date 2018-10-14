#!/usr/bin/env python

input_file = 'recycle-small.dat'

def cyclic_perms(num_digits):
    id_perm = range(0,num_digits)
    perm_list = [id_perm]
    for n in range(1, num_digits):
        perm_list.append([ id_perm[x] for x in range(0-n,num_digits-n)])
    
    return perm_list

with open (input_file, 'r') as data_file:
    N_tests = int(data_file.readline())
    
    for i in range(0, N_tests):
        (A, B) = map(int,data_file.readline().split())
        pairs = []
        num_pair = 0
       
        N_digits = len(map(int, str(A)))
        cycles = cyclic_perms(N_digits)
#        print cycles

        for j in range(A,B+1):
            digits = map(int, str(j))
            for cyc in cycles:
                P = [ digits[x] for x in cyc ]
                k = int(''.join(map(str, P)))            
                if (k >= A and k <= B and k != j):
                    if (not ((j,k) in pairs)):
                        pairs.append((j,k))
                        pairs.append((k,j))
                        num_pair += 1
        
        case_str = "Case #{0:d}: {1:d}".format(i+1, num_pair)
        print case_str
            