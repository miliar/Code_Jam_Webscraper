def check_tidy(i):
    l = [0]
    for j in list(str(i)):
        for k in l:
            if int(j) < k:
                return False
        l.append(int(j))
    return True

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n_str = input()  # read a list of integers, 2 in this case
    n = int(n_str)

    #print(n)
    temp_n = n_str
    a = list(temp_n)
    for j in range(1, len(n_str)):
        if check_tidy(int(temp_n)):
            break
        if not check_tidy(int(temp_n)) or int(temp_n) >= n:
            #print(list(temp_n))
            a = list(temp_n) 
            a[-j] = "9"
            a[len(n_str)-j-1] = str(int(a[len(n_str)-j-1]) - 1)
            if int(a[len(n_str)-j-1]) < 0:
                a[len(n_str)-j-1] = str(int(a[len(n_str)-j-1]) + 1)
            #print(a)
            temp_n = "".join(a)

    #a = list(temp_n)
    #a[0] = str(int(a[0]) - 1)
    temp_n = "".join(a)

    print("Case #{}: {}".format(i, str(int(temp_n))))

