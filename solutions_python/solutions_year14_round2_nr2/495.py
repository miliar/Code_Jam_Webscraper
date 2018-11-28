f = open('B-small-attempt0.in', 'r')
outf = open('output1.txt', 'w')

T = int(f.readline())

def small_and(A, B, K):
    total_num = 0
    for i in range(A):
        for j in range(B):
            if i & j < K:
                total_num += 1
    return total_num

for test_ind in range(T):
    A, B, K = map(int, f.readline().split())
    total_num = small_and(A, B, K)
    out_str = 'Case #' + str(test_ind + 1) + ': ' + str(total_num) + '\n'
    outf.write(out_str)

f.close()
outf.close()
