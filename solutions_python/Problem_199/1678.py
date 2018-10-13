def solution(a, n):
    res = 0
    flag = True
    for ii in range(len(a)):
        flag = flag & (a[ii] == '+')
    if flag == True:
        return 0

    for ii in range(len(a) - n + 1):
        if a[ii] == '-':
            res += 1
            for jj in range(n):
                if a[ii + jj] == '+':
                    a[ii + jj] = '-'
                else:
                    a[ii + jj] = '+'

    for ii in range(len(a)):
        if a[ii] == '-':
            return 'IMPOSSIBLE'
    return res


if __name__ == '__main__':
    num = 0
    src_handle = open('A-large.in', 'r')
    dst_handle = open('large_output', 'w')
    for line in src_handle:
        if num == 0:
            num += 1
            continue
        line = line.strip('\n').split(' ')
        a = list(line[0])
        n = int(line[1])
        res = solution(a, n)
        text = 'Case #' + str(num) + ': ' + str(res) + '\n'
        dst_handle.write(text)
        num += 1
    src_handle.close()
    dst_handle.close()

    # '+-++ 2'
    # a = list('+-++')
    # n = 2
    # print(solution(a, n))