import string
import sys
m = {}
m['q'] = 'z'
m['e'] = 'o'
m['y'] = 'a'
inputs  ="""ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
outputs = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""
#"""
for (line_in, line_out)  in zip(inputs.split("\n"), outputs.split("\n")):
    #print len(line_in), len(line_out)
    for (c_in, c_out) in zip(line_in, line_out):
        if c_out != ' ':
            if c_in in m:
                if not( m[c_in] == c_out):
                    print "bad!"
            else:
                m[c_in] = c_out


all_letters = set(string.ascii_lowercase)
missing_in = list(all_letters - set(m.keys()))[0]
missing_out = list(all_letters - set(m.values()))[0]
m[missing_in] = missing_out
#print m                
m[' '] = ' '

n = int(sys.stdin.readline())
for i in range(1, n+1):
    line_in = sys.stdin.readline().strip()
    line_out = "".join([m[c] for c in line_in])
    print "Case #%d: %s" % (i, line_out)
