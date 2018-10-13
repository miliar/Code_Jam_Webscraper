import pprint
import codecs
import copy

def rot(d, n):
    #print "d: " + str(d) + " " + "n: " + str(n)
    nstr = str(n)
    l = len(nstr)
    end = nstr[l-d:l]
    beg = nstr[0:l-d]
    return int(end + beg)

file = codecs.open("recycled.small.in", encoding="utf-8", mode="r")
outfile = codecs.open("recycled.small.out", encoding="utf-8", mode="w")
totalCases = int(file.readline())
for case in range(totalCases):
    line = file.readline().rstrip('\n').split(' ')
    A = int(line[0])
    B = int(line[1])
    print "A: " + str(A) + " " + "B: " + str(B)
    answer = []
    for x in range(1, len(str(A))):
        for n in range(A, B+1):
            m = rot(x, n)
            if m > n and n >= A and m <= B and len(str(m)) == len(str(n)) and (n,m) not in answer:
                print "Found n: " + str(n) + " " + "m: " + str(m)
                #print str(m)
                answer.append((n,m))
        print ""
    print "Case #" + str(case+1) + ": " + str(len(answer))
    outfile.write("Case #" + str(case+1) + ': ' + str(len(answer)) + '\n')
