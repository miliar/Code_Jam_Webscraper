f = open("A-large.in")
fw = open("A-large.txt", 'w+')

testCases = 0   # test cases in the input file

first_line = f.readline()
testCases = int(first_line)

def flipStringTo(S, fromIndex, K):
    listStr = []
    for i in xrange(0, len(S)):
        listStr.append(S[i])
        pass

    for i in xrange(fromIndex, fromIndex + K):
        if listStr[i] == '-':
            listStr[i] = '+'
        else:
            listStr[i] = '-'
        pass
    return ''.join(listStr)

for case in xrange(0, testCases):

    line = f.readline()
    dataArr = line.split()

    S = dataArr[0]
    K = int(dataArr[1])

    is_it_possible = True
    flip_count = 0

    for i in xrange(0, len(S)):

        if S[i] == '-':
            if len(S) - i < K:
                fw.write('Case #{}: {}\n'.format(case + 1, "IMPOSSIBLE"))
                is_it_possible = False
                break
            S = flipStringTo(S, i, K)
            flip_count += 1
        pass
    
    if is_it_possible:
        fw.write('Case #{}: {}\n'.format(case + 1, flip_count))
    pass
f.close()
fw.close()
