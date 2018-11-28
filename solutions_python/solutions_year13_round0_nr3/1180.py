import itertools
import os

def gen_palindromes():
    palindromes = range(1, 10)
    for k in range(2, 15):
        palindromes += [sum([n*(10**i) for i,n in enumerate(([x]+list(ys)+[z]+list(ys)[::-1]+[x]) if k%2
            else ([x]+list(ys)+list(ys)[::-1]+[x]))])
             for x in range(1,10)
             for ys in itertools.permutations(range(10), k/2-1)
             for z in (range(10) if k%2 else (None,))]
    palindromes_set = set(palindromes)
    return [x * x for x in palindromes if x * x in palindromes_set]

#print gen_palindromes()
p = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1234321, 123454321, 125686521]
def count(r):
    return len([1 for x in p if r[0] <= x <= r[1]])

fin = open('input', 'r')
fout = open('output', 'w')
for c in range(int(fin.readline())):
    fout.write('Case #{0}: {1}\n'.format(c + 1, count(map(int, fin.readline().split()))))
