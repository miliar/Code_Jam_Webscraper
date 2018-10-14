# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def check_start_end(S):
    start = -1
    end = -1;
    for pos in range(0, len(S)):
        if(start == -1 and S[pos] == '-'):
            start = pos
        if(S[pos] == '-'):
            end = pos
    return (start, end)

def flip(S, K, start):
    newS = S
    for i in range(start, start+K):
        if(newS[i] == '-'):
            newS = '%s%s%s'%(newS[:i],'+',newS[i+1:])
        else:
            newS = '%s%s%s'%(newS[:i],'-',newS[i+1:])
    return newS

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    splited = raw_input().split(" ")
    S = splited[0]
    K = int(splited[1])
    num = 0
    while True:
        start, end = check_start_end(S)
        if(start == -1 and end == -1):
            break
        if((end - start) < K-1):
            num = 'IMPOSSIBLE'
            break
        num += 1
        S = flip(S, K, start)
    print('Case #' + str(i) + ': ' + str(num))

    # check out .format's specification for more formatting options


