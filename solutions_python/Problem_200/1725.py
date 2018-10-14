def tidy(n):
    for i in range(len(n)-1):
        if n[i+1] < n[i]:
            for j in range(i, 0, -1):
                if n[i-1] < n[i]:
                    return n[:i] + str(int(n[i])-1) + '9'*(len(n)-i-1)
            if n[0] == '1':
                return '9' * (len(n)-1)
            else:
                return str(int(n[0])-1) + '9'*(len(n)-1)
    return n


if __name__ == '__main__':
    with open('output.out', 'w') as out:
        input()
        case = 0
        while True:
            case += 1
            try:
                n = input()
            except:
                break
            ans = tidy(n)
            ans_str = 'Case #{:}: {:}\n'.format(case, ans)
            out.write(ans_str)
            print(n, ans_str, end='')
