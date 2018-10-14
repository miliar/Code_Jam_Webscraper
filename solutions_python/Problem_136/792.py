def cookie_clicker (C, F, X):
    cookies_per_second = 2
    total_time = 0
    while True:
        time_at_C = C / cookies_per_second
        total_time += time_at_C
        time_after_C = (X - C) / cookies_per_second
        if time_after_C > X / (cookies_per_second + F):
            cookies_per_second += F
        else:
            total_time += time_after_C
            return total_time



f = open ('cookieLargeIN.in', 'r')
g = open ('cookieLargeOUT.txt', 'w')
numCases = int(f.readline())
for case in xrange (1, numCases + 1):
    line = f.readline().split()
    C, F, X = map(lambda x: float(x), line)
    g.write ('Case #' + str(case) + ': ' + str(cookie_clicker (C, F, X)) + '\n')
g.close()
f.close()
