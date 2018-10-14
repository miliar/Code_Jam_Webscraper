from __future__ import print_function
import sys

T = int(raw_input())

def customPrint2(S):
    customPrint(S,printer=sys.stdout.write)

def customPrint(S, printer=print):
    for i in xrange(len(S)):
        if S[i] == '0':
            continue
        else:
            printer(''.join(S[i:]))
            break

for t in xrange(T):
    sys.stdout.write('Case #{}: '.format(t+1))
    sys.stdout.flush()
    S = list(str(raw_input()))

    if len(S) == 1:
        customPrint(S)
    else:
        for i in xrange(1,len(S)):
            if int(S[i-1])>int(S[i]):
                for j in xrange(i-1, -1, -1):
                    #print('j = {}'.format(j))
                    temp = int(S[j]) - 1
                    if temp < 0:
                        S[j] = '9'
                    else:
                        if j > 0 and int(S[j-1])>temp:
                            S[j] = '9'
                            continue
                        else:
                            S[j] = str(temp)
                            break

                #sys.stdout.write(''.join(S[0:i]))
                customPrint2(S[0:i])
                sys.stdout.flush()
                print('9' * (len(S)-i))
                break
        else:
            customPrint(S)
