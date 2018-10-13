import sys


with open(sys.argv[1], 'r+') as param_file:
    data = param_file.read().splitlines()


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
    last_number = int(data[test])
    number = last_number
    output = 0
    digits = map(int, list(str(number)))
    while output == 0:
        if sorted(digits) == digits:
            output = map(str, digits)
            print output
            break
        for i in range(len(digits)-1):
            if digits[i] > digits[i+1]:
                digits[i] -= 1
                for k in range(i+1, len(digits)):
                    digits[k] = 9
                break
        #print digits


    with open('output.txt', 'a+') as output_file:
        output_file.write('Case #'+ str(test) + ': ' + str(int(''.join(output))) + '\n')
