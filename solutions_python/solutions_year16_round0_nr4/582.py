import sys

temp = sys.stdout
sys.stdout = open(r'C:\Users\Spin\Desktop\o.txt', 'a')

# Q = open(r'C:\Users\Spin\Desktop\t.txt')
Q = open(r'C:\Users\Spin\Desktop\D-small-attempt0.in')
T = int(Q.readline())


# def q1(n):
#     if n is 0:
#         return 'INSOMNIA'
#
#     pool = set('1234567890')
#     c = 1
#     while pool:
#         for digit in str(c*n):
#             if digit in pool:
#                 pool.remove(digit)
#
#         c += 1
#     return (c-1)*n

# def q2(s):
#     m = len(s)
#     l = []
#     for i in range(m):
#         if i is 0 or s[i] != l[-1]:
#             l.append(s[i])
#     if l[-1] == '+':
#         l.pop()
#     return len(l)

def q4small(k, c, s):
    # print(k, c, s)
    return ' '.join(map(str, range(1, k+1)))


for i in range(T):
    print('Case #%r:' % (i + 1), end=' ')
    q = map(int, Q.readline().split())
    # print(q1(n))
    print(q4small(*q))


sys.stdout = temp
