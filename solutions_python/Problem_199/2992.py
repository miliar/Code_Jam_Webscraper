import sys


with open(sys.argv[1], 'r+') as param_file:
    data = param_file.read().splitlines()

#print data

tests = int(data[0])


def convert(S, i, K):
    S = list(S)
    #print "S: ", S

    for k in range(int(K)):
        #print 'Index: ' + str(i+k)
        if S[i+k] == '+':
            S[i+k] = '-'
        elif S[i+k] == '-':
            S[i+k] = '+'

    return ''.join(S)

for test in range(1, tests + 1):
    test_case = data[test].split(' ')
    S = test_case[0]
    K = test_case[1]
    flips = 0
    for i in range(len(S)-int(K)+1):
        if S[i] == '-':
            S = convert(S, i, K)
            flips += 1

    if '-' in S:
        output = 'IMPOSSIBLE'
    else:
        output = str(flips)

    with open('output.txt', 'a+') as output_file:
        output_file.write('Case #'+ str(test) + ': ' + output + '\n')
