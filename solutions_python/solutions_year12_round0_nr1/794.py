import sys
import getopt
import re

ALPHA = "abcdefghijklmnopqrstuvwxyz"
forward = {}
backward = {}


encrypt = {' ': ' ', 'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'f': 'w', 'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u', 'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 'p': 'v', 's': 'd', 'r': 'p', 'u': 'j', 't': 'r', 'w': 't', 'v': 'g', 'y': 'a', 'x': 'h','z':'q','q':'z'}
decrypt = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z':'q','q':'z'}

def temp():
 
    plaintext = ["our language is impossible to understand",
                 "there are twenty six factorial possibilities",
                 "so it is okay if you want to just give up"]
    ciphertext = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
         "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
         "de kr kd eoya kw aej tysr re ujdr lkgc jv"]

    for p,c in zip(plaintext,ciphertext):
        for i in range(len(p)):
            if not forward.has_key(p[i]):
                forward[p[i]] = c[i]
            if not backward.has_key(c[i]):
                backward[c[i]] = p[i]


    print forward
    print backward

def process(ciphertext):
    str = ""
    for letter in ciphertext:
        str += decrypt[letter]
    return str

if __name__ == "__main__":

    f = open('A-small-attempt1.in','r')
    f.readline()
    i = 0
    for line in f:
        i = i+1
        pr = "Case #"
        pr += str(i)
        pr += ": "
        pr += process(line.strip())
        print pr


    


