import re

def make_pattern(testword):
    pattern = r''
    
    for c in testword:
        if c == "(":
            pattern += "["
        if c == ")":
            pattern += "]"
        else:
            pattern += c
    
    return pattern


f = open("A-large.in")
lines = [line[:-1] for line in f]
f.close()

num_pattern = re.compile(r'\d+')
num_params = [int(x) for x in num_pattern.findall(lines[0])]

L = num_params[0]
D = num_params[1]
N = num_params[2]

words = ""
for word in lines[1:D+1]:
    words += word + " "

for n in xrange(D+1,D+1+N):
    pattern_string = lines[n]
    search = re.compile(make_pattern(pattern_string))
    count = 0
    print "Case #" + str(n - D) +":",
    for result in search.finditer(words):
        count += 1
    
    print count