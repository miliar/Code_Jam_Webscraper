n = int(raw_input())

welphrase = "welcome to code jam"


def nascendingseq(occurdict, phrase, pos):
    if phrase == "":
        return 1
    c = phrase[0]
    num = 0
    for i in occurdict[c]:
        if i > pos:
            if memoization.has_key((phrase[1:], i)):
                num += memoization[(phrase[1:], i)]
            else:
                num += nascendingseq(occurdict, phrase[1:], i)
    memoization[(phrase, pos)] = num
    return num

for i in range(n):
    s = raw_input()
    occurdictionary = {}
    memoization = {}

    for j in welphrase:
        if not occurdictionary.has_key(j):
            occurdictionary[j] = []
            for k in range(len(s)):
                if s[k] == j:
                    occurdictionary[j].append(k)
    print "Case #%d: %04d"%(i + 1, nascendingseq(occurdictionary, welphrase, -1) % 10000)

