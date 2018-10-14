def tidy(n):
    num = str(n)
    for i in range(1, len(num)):
        if num[i] < num[i-1]:
            return False
    return True

def min_1(k):
    if k == '1':
        return ''
    elif k[-1] > '0':
        return k[:-1]+(chr(ord(k[-1])-1))
    else:
        return min_1(k[:-1])+'9'

def solution(k):
    ret = ''
    while(k):
        if tidy(k):
            ret = k + ret
            break
        k = min_1(k[:-1])
        ret = '9' + ret
    return ret

K = int(input())
for i in range(K):
    k = input()
    print('Case #{0}: {1}'.format(i+1, solution(k)))
