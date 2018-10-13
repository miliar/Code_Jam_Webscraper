def number_finder(given_list):
    fix_it = False
    for i in range(len(given_list) - 1):
        if given_list[i] > given_list[i + 1] and not fix_it:
            fix_it = True
            given_list[i] -= 1
        elif fix_it:
            given_list[i] = 9
    if fix_it:
        given_list[-1] = 9
        return number_finder(given_list)
    else:
        return given_list

t = int(input())
for x in range(1, t+1):
    n = input()
    l = [int(x) for x in n]
    l = number_finder(l)
    if not l[0] and len(l) > 1:
        l = l[1:]
    n = ''.join(str(x) for x in l)
    prn_str = "Case #{}: {}".format(x, n)
    print (prn_str)
