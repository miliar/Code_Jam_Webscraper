import sys

temp = sys.stdout
sys.stdout = open(r'C:\Users\Spin\Desktop\o.txt', 'w')

Q = open(r'C:\Users\Spin\Desktop\t.txt')
T = int(Q.readline())

def sol(num):
    if num <= 9:
        return num

    s = str(num)
    n = len(s)

    for i in range(1, n):
        if s[i] < s[i-1]:
            break

    else:
        return num

    for j in range(i-1, -1, -1):
        if j == 0 or s[j-1] < s[j]:
            break

    res = s[:j] + str(int(s[j]) - 1) + '9' * (n - j - 1)
    return int(res)


for line in range(T):
    num = int(Q.readline())
    res = sol(num)
    print('Case #%r:' % (line + 1), res)

sys.stdout = temp
