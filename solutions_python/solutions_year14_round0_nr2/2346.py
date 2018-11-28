from decimal import *
getcontext().prec = 7
def findOut(arr):
    c,f,x = arr
    tr = 0.0000000
    current_rate_of_cookie_production = 2.0
    while True:
        time_to_c_cookies = c/current_rate_of_cookie_production
        time_to_total = x / current_rate_of_cookie_production
        time_after_buying = time_to_c_cookies + x / (current_rate_of_cookie_production+ f)
        if(time_to_total <= time_after_buying):
            tr += time_to_total
            break
        current_rate_of_cookie_production += f
        tr +=time_to_c_cookies
    return "{0:.7f}".format(tr)


def run():
    t = input()
    c = 1
    while(t>0):
        t-=1
        arr1 = map(float, raw_input().split())
        print "Case #" + str(c) + ": " + findOut(arr1)
        c+=1
run()