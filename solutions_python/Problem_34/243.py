f = open("alien_in.txt")
data = f.read()
f.close()

data = data.split("\n")

l, d, n = data[0].split(" ")
l, d, n = int(l), int(d), int(n)

data = data[1:-1]

#print l, d, n

words = data[0:d]
cases = data[d:d+n]

def unique(l):
    if l == []: return []
    l.sort()
    l2 = [l[0]]
    for i in xrange(1, len(l)):
        if l[i] != l[i-1]:
            l2 += [l[i]]
    return l2

def wordsWith(words, letter, pos):
    ws = []
    for word in words:
        if word[pos] == letter:
            ws += [word]
    return ws


def splitCase(word):
    i = 0
    ls = []
    letters = []
    while i < len(word):
        if 'a' <= word[i] and word[i] <= 'z':
            ls += [ [word[i]] ]
        else:
            if word[i] == '(':
                i += 1
                while word[i] != ')':
                    letters += [ word[i] ]
                    i += 1
                ls += [ letters ]
                letters = []
        i += 1
    return ls

def getCases(case, words):
    caseLetters = splitCase(case)
    for i in xrange(len(caseLetters)):
        ws = []
        for letter in caseLetters[i]:
            ws += wordsWith(words, letter, i)
        words = unique(ws)
    return len(ws)

"""
print words
print cases
"""

s = ""
for i in xrange(len(cases)):
    if i % 1 == 0:
        print float(i) / len(cases) * 100.0
    s += "Case #%d: %d" % (i+1, getCases(cases[i], words)) + "\n"

print s

f = open("alien_out.txt", "w")
f.write(s)
f.close()
