import re

f = open('A-large.in')

firstline = f.readline()
firstline = firstline.replace('\n', '').split(' ')
wordlength = int(firstline[0])
wordcount = int(firstline[1])
testcasecount = int(firstline[2])

wordslist = []

print wordcount
for i in range(wordcount):
    word = f.readline()
    wordslist.append(word)

wordsjoined = '|'.join(wordslist)

output = []
print wordsjoined
for i in range(testcasecount):
    test = f.readline()
    pattern = test.replace('(', '[').replace(')', ']')
    found = re.findall(pattern, wordsjoined)
    count = len(found)
    output.append('Case #%s: %s' % (str(i+1), count)) 
f.close()

out = open('Output A.out', 'w')
out.write('\n'.join(output))
out.close()
