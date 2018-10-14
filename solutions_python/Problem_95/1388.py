#!/usr/bin/env python



dic = {'e':'o', ' ':' ', 'a':'y', 'b':'h', 'y':'a', 'i':'d', 'r':'t', 'd':'s', 'c':'e', 'p':'r', 't':'w', 'j':'u','m':'l','s':'n','l':'g','k':'i','x':'m','v':'p','m':'l','h':'x','f':'c','w':'f','g':'v','n':'b','o':'k','z':'q','u':'j','q':'z','\n':''}
def bob(a):
    return dic[a]

file = open("input.in")
index = 0
for line in file:
    if(index!=0):
        print "Case #" + str(index) + ": " + ''.join(map(bob,line))
    index+=1



