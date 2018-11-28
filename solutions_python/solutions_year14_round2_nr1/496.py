def iround(x):
    """iround(number) -> integer
    Round a number to the nearest integer."""
    return int(round(x) - .5) + (x > 0)

def reduced(word):
    if word == "":
        return ""
    newword = word[0]
    for x in word[1:]:
        if x != newword[-1]:
            newword = newword + x
    return newword


f = open("data.txt", 'r')
g = open("data1.txt", 'w')
t = int(f.readline())
for k in range(1, t+1):
    N = int(f.readline())
    strings = []
    fail = False
    for i in range(N):
        word = f.readline()
        if word[-1] == '\n':
            word = word[:-1]
        strings.append(word)
    reducedstrings = [reduced(x) for x in strings]
    if len(set(reducedstrings)) > 1:
        fail = True
    print len(set(reducedstrings))
    if fail:
        g.write("Case #%d: Fegla won\n" % k)
        continue

    result = 0
    while strings[0] != "":
        firstletter = strings[0][0]
        array = []
        for j in range(len(strings)):
            count = 0
            i = 0
            while i < len(strings[j]) and strings[j][i] == firstletter:
                i += 1
                count += 1
            array.append(count)
            strings[j] = strings[j][i:]
        average = iround(sum(array) / (len(array)+0.0))
        for x in array:
            result += abs(x - average)

    g.write("Case #%d: %d\n" % (k, result))
f.close()
g.close()