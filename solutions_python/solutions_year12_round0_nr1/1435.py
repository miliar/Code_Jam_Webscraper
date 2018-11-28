input_file = 'A-small-attempt0.in'
output_file = "small_out.txt"

googlese = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''

english = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''

mapping = {
    'y': 'a',
    'e': 'o',
    'q': 'z',
    'z': 'q',
}
for i in range(len(googlese)):
    mapping[googlese[i]] = english[i]

#for key in sorted(mapping.iterkeys()):
#    print "%s: %s" % (key, mapping[key])

#for key, value in sorted(mapping.iteritems(), key=lambda (k,v): (v,k)):
#    print "%s: %s" % (key, value)

input = open(input_file, 'r')
output = open(output_file, 'w')

# number of cases
t = int(input.readline())

def solve(input_line):
    return ''.join([mapping[c] for c in input_line])

for i in range(t):
    line = input.readline()
    english = solve(line)
    output_line = "Case #%s: %s" % (i+1, english)
    output.write(output_line)

input.close()
output.close()
