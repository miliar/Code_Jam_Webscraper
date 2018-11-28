import sys

inputs = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
          "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
          "de kr kd eoya kw aej tysr re ujdr lkgc jv"]

outputs = ["our language is impossible to understand",
           "there are twenty six factorial possibilities",
           "so it is okay if you want to just give up"]

m = {' ': ' ',
     'z': 'q',
     'q': 'z'}


for i,o in zip(inputs, outputs):
    for k, v in zip(i, o):
        if k != ' ':
            m[k] = v

def translate(s):
    return "".join([m[v] for v in s])

sys.stdin = open('A-small-attempt1.in')
sys.stdout = open('output', 'w')

inputs = int(raw_input())
for i in xrange(inputs):
    s = raw_input()
    print "Case #%s: %s" % (i+1, translate(s))
