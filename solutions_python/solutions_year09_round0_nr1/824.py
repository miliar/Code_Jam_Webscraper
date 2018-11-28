l, d, n = [int(i) for i in raw_input().split(' ')]
words = []

def match(testcase, word):
    pos = 0
    group = None
    nummatches = 0
    
    for letter in testcase:
        if letter == '(':
            group = []
            continue
        elif letter == ')':
            if word[pos] in group:
                nummatches += 1
            group = None
        elif group != None:
            group.append(letter)
            continue
        elif word[pos] == letter:
            nummatches += 1
        pos += 1
    return len(word) == nummatches


for i in range(d):
    words.append(raw_input())

for i in range(n):
    testcase = raw_input()
    nummatches = 0
    for word in words:
        if match(testcase, word):
            nummatches += 1
    print 'Case #%d: %d' % (i + 1, nummatches)

