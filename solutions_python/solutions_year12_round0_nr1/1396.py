#!/usr/bin/python2

"""
a = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"
b = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"
m = {'q' : 'z', 'z' : 'q', ' ' : ' ' }
for i in range(len(a)) :
    m[a[i]] = b[i]

c = "abcdefghijklmnopqrstuvwxyz"
print repr(m)
"""

trans = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

T = int(raw_input())
for t in xrange(T) :
    s = raw_input()
    ss = ''.join([trans[i] for i in s])
    print 'Case #%d:' % (t + 1), ss
