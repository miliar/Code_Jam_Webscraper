import sys

i = open("A-small-attempt0.in", "r")
T = int(i.readline())
d={' ':' ','a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
for X in range(T):
    G = i.readline().strip()
    S=''
    for ch in G:
        S += d[ch]
    print "Case #" + str(X+1) + ": " + S
        