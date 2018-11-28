def solve():
    n = int(input())

    for i in range(n):
        string_number = input()
        digits = (['Z', 'E', 'R', 'O'],
                  ['T', 'W', 'O'],
                  ['S', 'I', 'X'],
                  ['E', 'I', 'G', 'H', 'T'],
                  ['T', 'H', 'R', 'E', 'E'],
                  ['F', 'O', 'U', 'R'],
                  ['F', 'I', 'V', 'E'],
                  ['O', 'N', 'E'],
                  ['S', 'E', 'V', 'E', 'N'],
                  ['N', 'I', 'N', 'E'])
        mapping = [0, 2, 6, 8, 3, 4, 5, 1, 7, 9]
        ans = ""
        input_list = list(string_number)

        while len(input_list) > 0:
            for j in range(len(digits)):
                x = digits[j]

                has_all = True

                while has_all:
                    copy_list = list(input_list)
                    for k in range(len(x)):
                        if x[k] not in copy_list:
                            has_all = False
                            break
                        else:
                            copy_list.remove(x[k])
                    if has_all:
                        ans += str(mapping[j])
                        for k in range(len(x)):
                            input_list.remove(x[k])

        print("Case #%s: %s" % (i + 1, ''.join(sorted(ans))))


solve()
