attempt_list = ['B-test','B-small-attempt1','B-large']
attempt = attempt_list[2]

import time
time.clock()

def solve(n):

    # one-digit number is always tidy
    if n < 10:
        return n

    n2 = n
    inOrder = False
    while inOrder == False:
        digits = list(map(int,str(n2)))
        for i in range(0,len(digits)-1):
            if digits[i] > digits[i+1]:
                if digits[i] == 1:
                    # if all leading digits so far are 1s, result will be 9..9
                    return round(n,-len(str(n))+1)-1
                else:
                    # reduce the digit and change to 9s all the following digits
                    digits[i] -= 1
                    for j in range(i+1,len(digits)):
                        digits[j] = 9
                    n2 = int(''.join(str(x) for x in digits))
                    break
        inOrder = True
        for i in range(0,len(digits)-1):
            if digits[i] > digits[i+1]:
                inOrder = False
                break
    return n2


def main():
    fin = open(attempt + '.in', 'r')
    fout = open(attempt + '.out','w')

    numcases = int(fin.readline())

    for casenum in range(1,numcases+1):
        n = int(fin.readline())
        fout.write('Case #' + repr(casenum) + ': ' + str(solve(n)) + '\n')

    fin.close()
    fout.close()

main()
print(time.clock())