__author__ = 'amoscati'
import copy

f = open('input.txt')
output = open('output.txt', 'w')
lines = [ line for line in f]
T = int(lines[0])

decode = {'y': 'a', 'n':'b','f':'c','i':'d','c':'e','w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l','x':'m','s':'n','e':'o', 'v':'p','z':'q', 'p':'r','d':'s','r':'t', 'j':'u','g':'v','t':'w', 'h':'x', 'a':'y', 'q':'z', ' ': ' ', '\n': '\n'}
index = 1
while (index < len(lines)):
    t = 0
    while (t < T):
        t = t + 1
        G = lines[index]
        index = index + 1

        g = "".join([decode[c] for c in G])

        #print
        print 'Case #%d: %s' % (t,g)
        output.write('Case #%d: %s' % (t,g))




