import sys
import math

original = 'y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
target =   'a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

dic = {}
for o, t in zip(original, target):
    dic[o] = t

for i in range(26):
    let = chr(ord('a')+i)
    if let not in original:
        orig_missing = let
    if let not in target:
        targ_missing = let

dic[orig_missing] = targ_missing

#print len(dic)
#print orig_missing, targ_missing

def solve(line):
    res = ''
    for ch in line:
        res += dic[ch]
    return res

def readline():
    return input.readline().strip(' \r\n\t')

def do_test(input):
    line = readline()
    res = solve(line)
    return str(res)

input = sys.stdin

N = int(readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%d: %s' % (test+1, answer)
    sys.stdout.flush()
    
