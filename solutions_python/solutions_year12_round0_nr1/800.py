'''
Created on 2012/04/14

@author: hanaue51
'''
import os
os.chdir("../../../data/2012/qualification/")
filename = "A-small-attempt0"
postfix_in = ".in"
postfix_out = ".out"
format = "Case #%d: %s\n"

infile = open(os.getcwd() + "/" + filename + postfix_in, "r")
lines = infile.readlines()
infile.close()

alphabet_k = [chr(ord('a') + i) for i in xrange(26)]
alphabet_v = [chr(ord('a') + i) for i in xrange(26)]
encoding = {}
samples = {}
samples['ejp mysljylc kd kxveddknmc re jsicpdrysi'] = 'our language is impossible to understand'
samples['rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'] = 'there are twenty six factorial possibilities'
samples['de kr kd eoya kw aej tysr re ujdr lkgc jv'] = 'so it is okay if you want to just give up'
for key in samples:
    if len(key) == len(samples[key]):
        for i in xrange(len(key)):
            c = key[i]
            if not encoding.has_key(c) and c != ' ':
                encoding[c] = samples[key][i]
                del(alphabet_k[alphabet_k.index(c)])
                del(alphabet_v[alphabet_v.index(samples[key][i])])
encoding['q'] = 'z'
encoding['z'] = 'q'

n_cases = int(lines[0].strip())
results = []
for i in xrange(1, len(lines)):
    line = lines[i].strip()
    answer = ''
    for c in line:
        if encoding.has_key(c):
            answer += encoding[c]
        else:
            answer += c
    results.append(format % (i, answer))

#print results
outfile = open(os.getcwd() + "/" + filename + postfix_out, "w")
for result in results:
    outfile.write(result)
outfile.close()
