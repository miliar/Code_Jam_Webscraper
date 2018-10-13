def prev_tidy_number():
    n = list(input())
    for i in range(len(n) - 1, 0, -1):
        if n[i] < n[i - 1]:
            for j in range(i, len(n)):
                if n[j] == '9':
                    break
                n[j] = '9'
            n[i - 1] = chr(ord(n[i - 1]) - 1)
    if n[0] == '0':
        n.pop(0)
    return ''.join(n)


for tc in range(1, int(input()) + 1):
    print(f'Case #{tc}:', prev_tidy_number())
