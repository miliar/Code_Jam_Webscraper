'''
Created on 14.04.2012

@author: speedyGonzales
'''
def main(line):
    cypher = {'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f', 'l':'g','b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l', 'x':'m', 's':'n','e':'o', 'v':'p', 'z':'q', 'p':'r', 'd':'s', 'r':'t', 'j':'u','g':'v', 't':'w', 'h':'x', 'a':'y', 'q':'z',' ':' '}
    res=[]
    for symbol in line:
        res.append(cypher[''+symbol])
    return ''.join(res)


if __name__ == '__main__':
    import sys
    N = int(sys.stdin.readline())
    for i in xrange(N):
        res = main(sys.stdin.readline().strip())
        print "Case #%d: %s" % (i + 1, res)
