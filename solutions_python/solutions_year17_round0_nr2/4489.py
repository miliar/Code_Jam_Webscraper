def tidy(n):
    n_lst = list(map(int, str(n)))
    n_len = len(n_lst)
    if n_len == 1:
        return n

    while n_lst != sorted(n_lst):
        for i in range(len(n_lst)-1):
            a, b = n_lst[i], n_lst[i+1]
            if a > b:
                n_lst[i] -= 1
                n_lst[i+1:] = [9] * (n_len - 1 - i)

    return int("".join(map(str, n_lst)))


if __name__ == '__main__':
    test_cases = int(input())
    for tc in range(test_cases):
        result_txt = "Case #" + str(tc + 1) + ": "
        print(result_txt, tidy(input()), sep="")
