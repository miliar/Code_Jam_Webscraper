nos = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001L, 10221412201L, 12102420121L, 12345654321L, 40000800004L, 1000002000001L, 1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L, 1024348434201L, 1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L, 1234567654321L, 4000008000004L, 4004009004004L]

import sys
sys.stdin = open('C-large-1.in', 'r')
sys.stdout = open('C-large-1.out', 'w')
out = sys.stdout
N = input()
for i in range(1, N+1):
    out.write('Case #')
    out.write(str(i))
    out.write(': ')

    (A, B) = raw_input().split(' ')
    A = int(A)
    B = int(B)
    cnt = 0
    for n in nos:
        if n >= A and n <= B:
            cnt += 1
    print cnt
sys.stdin.close()
sys.stdout.close()

