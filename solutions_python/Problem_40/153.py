import sys
import re

def input_line(ctors):
    return [x[0](x[1]) for x in zip(ctors,
        sys.stdin.readline().strip().split())]

def input_strs():
    return [x for x in sys.stdin.readline().strip().split()]

if __name__ == "__main__":
    (N,) = input_line((int,))
    for case in range(1, N+1):
        (L,) = input_line((int,))
        dt=''
        for line in range(L):
            dt += sys.stdin.readline().strip()
        (A,) = input_line((int,))
        animals=[]
        for a in range(A):
            animals.append(input_strs()[2:])

        dt = re.sub('[0-9.]+', lambda m:m.group(0)+',', dt)
        dt = re.sub('[a-z]+', lambda m:'"'+m.group(0)+'",', dt)
        dt = re.sub(r'\)', '),', dt)
        dt = eval(dt)[0]

        print "Case #%d:" % case
        for a in animals:
            p = 1.0 * dt[0]
            tree = dt
            while len(tree)>1:
                if tree[1] in a:
                    tree = tree[2]
                else:
                    tree = tree[3]
                p*=tree[0]
            print "%0.7f" % p
