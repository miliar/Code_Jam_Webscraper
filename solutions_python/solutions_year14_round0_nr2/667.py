def cookie_clicker_alpha(filename):
    file = open(filename)
    out = open("output.txt", "w+")
    testcases = int(file.readline())
    for test in range(0, testcases):
        C, F, X = file.readline().split(' ')
        C = float(C)
        F = float(F)
        X = float(X)
        rate = 2.0
        gen_time = X/rate

        time = C/rate
        cookies = C
        count = 0
        ans = gen_time
        while cookies < X:
            increment = 0
            if cookies >= C:
                rate += F
                cookies -= C
                count += 1
##                print(count)
                
            if ((X-cookies)/(rate+F)) + (C/rate) > (X/rate):
                increment = (X)/rate
                time += increment
                cookies += increment*rate
            else:
                increment = min([(X-cookies)/rate, (C/rate)])
                time += increment
                cookies += rate*increment
            cookies = round(cookies,7)
            if time < gen_time:
                ans = time    
            else:
                ans = gen_time
        ans = round(ans,7)
        final = ("Case #" + str(test+1) + ": " + str(ans) + "\n")
##        print(final)
        out.write(final)
    file.close()
    out.close()
