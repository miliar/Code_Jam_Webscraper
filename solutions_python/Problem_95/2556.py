'''
Created on Apr 13, 2012

@author: paulo
'''
def translate(word):
    outputString = ''
    for char in word:
        if char in dic_trans.keys():
            outputString += dic_trans[char]
        else:
            outputString += char
    return outputString

dic_trans = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q':'z', 'z':'q'}



N = int(raw_input())

for case in xrange(N):
    wordCripted = raw_input()
    print "Case #%d: %s" %(case + 1, translate(wordCripted))