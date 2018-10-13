##Repeater Problem



def repeater_sub (word):
    word = [i for i in word]
    result = []
    L = len (word)
    i = 0
    while i < L:
        count = 0
        key = word[i]
        while i < L and word[i] == key:
            count += 1
            i += 1
        result.append ([key, count])
    return result



def Repeater (A): ## N = 2
    first, second = A
    count = 0
    first = repeater_sub (first)
    second = repeater_sub (second)
    L = len (first)
    if len (second) != L:
        return 'Fegla Won'
    i = 0
    while i < L:
        if first[i][0] != second[i][0]:
            return 'Fegla Won'
        else:
            count += abs (first[i][1] - second[i][1])
        i += 1
    return str(count)


f = open ('input.txt', 'r')
g = open ('output.txt', 'w')
N = int (f.readline())
for case in xrange (1, N + 1):
    f.readline()
    A = []
    for _ in xrange (2):
        word = f.readline()
        A.append (word)
    solution = Repeater (A)
    print solution
    g.write ('Case #' + str (case) + ': ' + solution + '\n')
g.close()
f.close()
        
            