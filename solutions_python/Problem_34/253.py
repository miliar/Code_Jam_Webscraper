import sys;
import re;

def solve(words, regex):
    count = 0;
    for word in words:
        if re.match(regex, word):
            count = count + 1;

    return count;

f = open(sys.argv[1]);
line = f.readline();

vals = map(int, line.split(' '));
L = vals[0];
D = vals[1];
N = vals[2];

words = [];
for i in xrange(D):
    words.append(f.readline());

cases = [];
for i in xrange(N):
    cases.append(f.readline().replace('(', '[').replace(')',']'));

out = open(sys.argv[2], "w");
for i in xrange(N):
    K = solve(words, re.compile(cases[i]));
    out.write("Case #%d: %d\n" % ((i+1), K));
out.close();
