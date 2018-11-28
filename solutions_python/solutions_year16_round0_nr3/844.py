from math import sqrt
import os

def pFactors(n):
    """Finds one nontrivial factor 'n'"""

    flag = False
    pFact, limit, num = [], int(sqrt(n)) + 1, n
    if n == 1: return False,1
    check = 2
    limit = min(limit,100000)
    while check < limit:
        check += 1
        if num % check == 0:
            flag = True
            break
    return flag, check


def nontrivialFactor(coin,base):

    val = 0
    t = 0
    for bit in coin[::-1]:
        if bit == '1':
            val += base**t
        t += 1
    Feasible, check = pFactors(val)
    return Feasible, check


def nontrivialFactorAll(coin):

    Check = []
    Flag = True
    for base in range(2,11):
        flag,check = nontrivialFactor(coin,base)
        if flag:
            Check.append(check)
        else:
            Flag = False
            break

    return Flag,Check



def EnumerateAll(J):

    if os.path.exists('Bits32.out'):
        print 'removing file'
        os.remove('Bits32.out')
    count = 0
    output = open('Bits32.out','a')
    output.write('Case #1:\n')

    val = 2**31
    while val < 2**32:
        val += 1
        coin = "{0:032b}".format(val)
        if coin[0] != '1' or coin[-1] != '1':
            continue
        Flag,Check = nontrivialFactorAll(coin)
        if Flag :
            count += 1
            checkstr = ''
            for s  in Check:
                checkstr = checkstr + ' '+str(s)
            writeLine = coin + checkstr+'\n'
            output.write(writeLine)
            if count >= J:
                break
    output.close()


f = open('C-large.in', 'r')
Data = f.read()
Data = Data.split('\n')
Data = Data[1]

N = int(Data[0:2])
J = int(Data[3:6])
print N,J
if N == 32 and J == 500:
    print 'File Production Begins'
    EnumerateAll(500)
    print 'File Producation Completed'