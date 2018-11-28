x = int(input())


def is_tidy(lst):
    for c, b in zip(lst, lst[1:]):
        if c > b:
            return False
    return True


for k in range(1, x+1):
    largest_num = int(input())
    check = list(str(largest_num))
    check = [int(n) for n in check]

    while not is_tidy(check):
        for a in range(len(check) - 1):
            if check[a] > check[a + 1]:
                index = a + 1
                for t in range(index, len(check)):
                    check[t] = 0
                check = [str(n) for n in check]
                check = ''.join(check)
                check = int(check) - 1
                check = str(check)
                if '9' in check and len(set(check)) == 1:
                    break
                check = list(check)
                check = [int(n) for n in check]

    check = [str(n) for n in check]
    check = ''.join(check)
    print("Case #{}: {}".format(k, check))



