import sys
#https://docs.python.org/2/library/decimal.html
##from decimal import *
##getcontext().prec = 7

str_path="C:/Users/Ricky/Documents/1_CUNY_Queens_College/Courses/2014/Spring2014/CS780_AdvancedProgrammngTechniques/GoogleCodeJam/Q_Round/B-large.in"

with open(str_path) as f:
    test_cases = int(f.readline())
    for test_case in range(test_cases):
        #C = cost of a cookie farm
        #F = additional cookie gained after a cookie farm purchase
        #X = cookies needed on hand to win
        C, F, X = f.readline().split()
        C = float(C)
        F = float(F)
        X = float(X)
##        print C, F, X
        current_cookie_earning_rate = 2.0
        accumulated_time_used_farm_purchase = 0.0
        #time_a = time needed to win a game without any farm purchase; initially set to time needed to win a game without any purchase
        time_a = X / current_cookie_earning_rate
        #time_b = new time needed after buying a cookie farm; initially set to '-inf'
        time_b = float('-inf')
        previous_time_a = 0.0 #Store the time of prvious_time_a before increasing after farm purchase
        while time_b < time_a:
            if time_b > 0:
                time_a = time_b
            #calculate the new rates after buying a cookie farm and get time_b
            current_farm_purchase_rate = C / current_cookie_earning_rate
            accumulated_time_used_farm_purchase += current_farm_purchase_rate
            current_cookie_earning_rate += F
            time_b = X / current_cookie_earning_rate + accumulated_time_used_farm_purchase
##            print time_a, time_b
        output = time_a
        #http://stackoverflow.com/questions/255147/how-do-i-keep-python-print-from-adding-spaces
        sys.stdout.write('Case #')
        sys.stdout.write(str(test_case+1))
        sys.stdout.write(': ')
        print output
