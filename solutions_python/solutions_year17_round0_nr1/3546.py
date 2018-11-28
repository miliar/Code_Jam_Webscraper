import sys
def calc_panc(S, num, rem):
    count = 0
    while(1):
        if '-' in S:
            l = S.index('-')
        else:
            break
        if (len(S) - l) >= num:
            A = num
        else:
            return -999999
        for i in range(A):
            if S[l+i] == '-':
                S[l+i] = '+'
            else:
                S[l+i] = '-'
        if ''.join(S) in rem:
            return -999999
        else:
            rem.append(''.join(S))
        count += 1
    return count


T = int(raw_input())
inputs = list()
for i in range(T):
    inputs.append(raw_input())
    
print(inputs)
''' T is the number of test cases '''
for i in range(T):
    a = inputs[i].split(' ')
    rem = list()
    S = a[0]
    num = int(a[1])
    rem.append(S)
    iterat = calc_panc(list(S), num, rem)
    if iterat >= 0:  
        print("Case #" + str(i+1) + ": " + str(iterat))
    else:
        print("Case #" + str(i+1) + ": IMPOSSIBLE")
