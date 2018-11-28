#!/usr/bin/env python


mm = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z','z':'q',' ': ' ','\n': ''}

def str_tran(inp):
    string = ''
    for i in inp:
        string += mm[i]
    return string 


if __name__ == '__main__':
    f = open('input')
    a = int( f.readline() )
    for case in range(a):

        line = f.readline()


        result = str_tran(line)
        print "Case #"+str(case+1)+":", result
