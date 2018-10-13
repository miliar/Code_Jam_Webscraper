def largest_tidy(N):
    N_lst = list(str(N))
    N_len = len(N_lst)
    i = 0
    while i <= N_len - 2 and N_lst[i+1] >= N_lst[i]:
#        print("i = {}".format(i))
#        if N_lst[i+1] >= N_lst[i]:
            i = i+1
    if i == N_len - 1:
        return N
    elif N_lst[i] == N_lst[0]:
        N_lst[0] = str(int(N_lst[0]) - 1)
        for k in range(1, N_len):
            N_lst[k] = '9'
#        N_lst.pop()
        return int(''.join(N_lst))
    else:
        last_digit = N_lst[i]
        last_digit_int = int(last_digit)
        j = i
        while j >= 1 and N_lst[j-1] == last_digit:
#            print("j = {}".format(j))
            j = j - 1
        for k in range(j, i + 1):
            N_lst[k] = str(last_digit_int - 1)
        for k in range(i + 1, N_len):
            N_lst[k] = '9'
        return int(''.join(N_lst))

cases = int(input())

for t in range(1, cases + 1):
    N = int(input())
    largest = largest_tidy(N)
    print("Case #{}: {}".format(t, largest))
