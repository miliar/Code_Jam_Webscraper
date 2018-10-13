__author__ = 'thainguyen'

f = [
        ['GRRR','GGRR','GRRR','GGRR'],
        ['GGRR','GGRR','GGGR','GGRR'],
        ['GRRR','GGGR','GRGR','GGGG'],
        ['GGRR','GGRR','GGGG','GGRG']
]
res = {
    'G': 'GABRIEL',
    'R': 'RICHARD'
}

# fi = open('OminousOmino.in', 'r')
fi = open('D-small-attempt1.in','r')
# fi = open('D-large.in','r')
fo = open('OminousOmino.out', 'w')

tests = int(fi.readline())
for test_case in range(tests):
    line = fi.readline()
    x,r,c = tuple(map(int,line.split()))
    fo.write('Case #' + str(test_case+1) + ': ' + res[f[r-1][c-1][x-1]]+'\n')