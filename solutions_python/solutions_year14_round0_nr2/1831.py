def win_cookie_clicker(C, F, X):
    R = 2.0
    t_total = 0.0
    t_win_1 = X/R
    t_win_2 = C/R + X/(R+F)
    while(t_win_1 > t_win_2):
        t_total += C/R
        R = R + F
        t_win_1 = X/R
        t_win_2 = C/R + X/(R+F)
    t_total += X/R
    return t_total




data = open("cookie_clicker.in").readlines()

num_tests = int(data[0])

for i in range(num_tests):
    values = data[i+1].strip('\n').split()
    result = win_cookie_clicker(float(values[0]), float(values[1]), float(values[2]))
    print "Case #%s: %.7f" %(i+1, result)
