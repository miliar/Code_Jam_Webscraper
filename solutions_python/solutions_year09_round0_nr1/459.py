import re

fin = file("A-large.in", "r")
fout = file("A-large.out", "w")

L, D, N = [int(x) for x in fin.readline().split()]
words = []

for d in xrange(D):
    words.append(fin.readline().rstrip())

for caseno in xrange(N):
    case = fin.readline().rstrip().replace("(", "[").replace(")", "]")
    expr = re.compile(case)
    answer = 0
    for word in words:
        if expr.match(word):
            answer += 1
    fout.write("Case #%i: %i\n" % (caseno + 1, answer))

fin.close()
fout.close()
