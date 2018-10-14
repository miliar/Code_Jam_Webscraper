#!/usr/bin/python

import re

def main ():
    output_file = 'output.txt'
    input_file = 'C-small-attempt0.in'
    pattern = re.compile (r'^(\d)\1*$')
    zero_pattern = re.compile (r'^0')
    fout = open (output_file, 'w')
    c = 1
    recycle = []
    with open(input_file, 'r') as fin:
        count = int(fin.readline())
        for line in fin:
            input_values = line.split()
            A = int(input_values[0])
            B = int(input_values[1])
            #print A, B
            count = 0
            if len(str(A)) == 1:
                recycle.append (count)
            elif len(str(A)) != len(str(B)):
                recycle.append(count)
            else:
                num_dict = {}
                for m in range (B, A, -1):
                    str1 = str(m)
                    if not pattern.match(str1):
                        for i in range(1, len(str1)):
                            x = ''.join(str1[i:])
                            x += (str1[:i])
                            n = int(x)
                            if not (zero_pattern.match(str(m)) or zero_pattern.match(str(n))):
                                if (A <= n) and (n < m) and (m <= B):
                                    if n in num_dict.keys():
                                        num_dict[n].append(m)
                                    else:
                                        num_dict[n] = [m,]
                                    #else:
                                    #    print 'new', n, m
                                    #    num_dict[m] = [n]
                                    print B, m, n, A
                                    count += 1
                recycle.append(count)
                z = 0
                distinct_m = []
                for k, j in num_dict.iteritems():
                    print k, j
                    for o in j:
                        distinct_m.append(o)
                        if (A <= k) and ( k < o) and (o <= B):
                            pass
                        else:
                            print 'yabakhto'
               #     print k, j
                    z += len(j)
                distinct_m = set(distinct_m)
                #    z += len(j)
                #print z
                #for q in num_dict.keys():
                #    z += num_dict[q]
            fout.write('Case #%s: %s\n' %( c, recycle[c-1]))
            c += 1
    fout.close()

if __name__ == '__main__':
    main ()

