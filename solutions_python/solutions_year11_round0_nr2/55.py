import string
import time

infile = open('a.in','r')
outfile = open('a.out','w')

T = int(string.strip(infile.readline()))

for k in xrange(T):
    s = string.split(string.strip(infile.readline()))
    C = int(s[0])
    s = s[1:]
    combine = {}
    for i in xrange(C):
        triple = s[i]
        combine[triple[0:2]] = triple[2:3]
        combine[triple[1]+triple[0]] = triple[2:3]
    s = s[C:]

    D = int(s[0])
    s = s[1:]
    oppose = {}
    for i in xrange(D):
        pair = s[i]
        if pair[0] in oppose:
            oppose[pair[0]].append(pair[1])
        else:
            oppose[pair[0]] = [pair[1]]
        if pair[1] in oppose:
            oppose[pair[1]].append(pair[0])
        else:
            oppose[pair[1]] = [pair[0]]
    s = s[D:]

    N = int(s[0])
    s = s[1:]

    output = []
    for i in xrange(N):
        output.append(s[0][i])
        if len(output) > 1:
            if output[-2]+output[-1] in combine:
                new = combine[output[-2]+output[-1]]
                output = output[:-2]
                output.append(new)
        if len(output) > 0:
            if output[-1] in oppose:
                for j in xrange(len(output)-1):
                    if output[j] in oppose[output[-1]]:
                        output = []
                        break
    
    answer = '['
    for t in output:
        answer += t+', '
    if len(answer) > 1:
        answer = answer[:-2]
    answer += ']'
    outfile.write('Case #%d: %s\n' % (k+1,answer))
