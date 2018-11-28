"""
call googlerese on the multiline string with the string surrounded
by triple quotes, like so:

>>> from lang import *
>>> googlerese(\"""3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv\""")

"""

def googlerese(stuff): 
    num_cases = stuff.split('\n')[0]
    translate = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
    i = 1
    splitStr = stuff.split('\n')
    while i < len(splitStr):
        ans = "Case #" + str(i) + ": "
        for letter in splitStr[i]:
            ans += translate[letter]
        print(ans)
        i+=1
    
