def solution(N):
    a = list(str(N))
    for ii in range(len(a))[::-1]:
        for jj in range(ii)[::-1]:
            if a[ii] < a[jj]:
                a[jj] = str(int(a[jj]) - 1)
                for kk in range(jj+1, len(a)):
                    a[kk] = '9'
                break

    return int(''.join(a))

# def solution_B(N):
#     while N >= 0:
#         a = list(str(N))
#         if len(a) == 1:
#             return N
#         flag = True
#         for ii in range(len(a) - 1):
#             flag = flag & (a[ii] <= a[ii + 1])
#         if flag == True:
#             return N
#         N = N - 1

if __name__ == '__main__':
    # a = '111111111111111110'
    # print(solution(a))
    # a = 1000
    # print(solution(a))


    num = 0
    src_handle = open('B-large.in', 'r')
    dst_handle = open('B_large_output', 'w')
    for line in src_handle:
        if num == 0:
            num += 1
            continue
        line = line.strip('\n')
        N = int(line)
        res = solution(N)
        text = 'Case #' + str(num) + ': ' + str(res) + '\n'
        dst_handle.write(text)
        num += 1
    src_handle.close()
    dst_handle.close()