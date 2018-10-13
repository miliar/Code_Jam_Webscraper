import sys

def solve(s, f):
    wG = ''
    for c in s:
	wG += f[c]

    return wG


def main(input_file, out_file):
    f = open(input_file, 'r')
    g = open(out_file, 'w')
    mapping = {}
    trainG = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
    rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
    de kr kd eoya kw aej tysr re ujdr lkgc jv'''
    trainL = '''our language is impossible to understand
    there are twenty six factorial possibilities
    so it is okay if you want to just give up'''
    mapping['q'] = 'z'
    mapping['z'] = 'q'

    for i in range(len(trainG)):
	if trainG[i] not in mapping:
	    mapping[trainG[i]] = trainL[i]
	    
   
    T = int(f.readline())

    for i in range(T):
        testcase = f.readline()
        sol = solve(testcase, mapping)
        #print 'Case #{0}: {1}'.format(i+1, sol)
        g.write('Case #{0}: {1}'.format(i+1, sol))
    f.close()
    g.close()

if __name__ == "__main__":
    main('input.txt', 'output.txt')


