f_in = open('input.txt')
f_out = open('output2.txt', 'w')
t = int(f_in.readline())

for testcase in range(t):
    a, b, k = map(int, f_in.readline().split())
    cnt = 0
    print testcase
    for i in range(a):
        for j in range(b):
            if i & j < k:
                cnt += 1

    answer = cnt
    f_out.write('Case #{0}: {1}\n'.format(testcase + 1, answer))

f_out.close()
