import re

# input
# data is copied by hand
# data = ''

data = data.split()

L = int(data[0])
D = int(data[1])
N = int(data[2])
words = data[3:D+3]
pattern = data[D+3:]

for t,p in enumerate(pattern):
    count = 0
    tmp = p.replace('(', '[')
    tmp = tmp.replace(')', ']')
    for w in words:
        if re.match(tmp, w) != None:
            count += 1
    print 'Case #' + str(t+1) + ': ' + str(count)



