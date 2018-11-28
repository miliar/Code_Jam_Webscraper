
import sys

def pre_num(ch):
    if ch == '0':
        return '9'
    else:
        return str(int(ch)-1)

def pre_tidy(number):
    lst_ln = len(number)-1

    for i in range (lst_ln-1,-1,-1):
        if int(number[i]) > int(number[i+1]):
            number[i] = pre_num(number[i])
            for j in range(i+1,len(number)):
                number[j] = '9'

    return ''.join(number)

def isTidy(number):
    prev_ch = number[0]
    for ch in number:
        if ch < prev_ch:
            return False
        prev_ch = ch
    return True


outf = open('B.out', 'w')

with open('B.in') as f:
    T = f.readline()

    for i in range(1,int(T)+1):
        N = f.readline()
        tidyNum = 0
        N = str(int(N))

#        for j in range(int(N),-1,-1):
#            if isTidy(str(j)):
#                tidyNum = j
#                break

        print("Case #%s: %s"%(str(i), str(int(pre_tidy(list(N))))))

outf.close()