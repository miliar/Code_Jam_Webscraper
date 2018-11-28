
cases=int(raw_input())

def how_much_time(c,f,x, cookies_per_second):
    
    curMinTime = x / cookies_per_second
    prevMinTime = curMinTime + 1
    extras=[]
    

    while prevMinTime > curMinTime:
        
        timeNoFactory = x / cookies_per_second
        timeForFactory = c / cookies_per_second

        extras.append(timeForFactory)

        new_cookies_per_second = cookies_per_second + f
        newTimeNoFactory = x / new_cookies_per_second
        
        t = curMinTime
        prevMinTime = t

        curMinTime = newTimeNoFactory + sum(extras)
        cookies_per_second = new_cookies_per_second
    
    return prevMinTime

for i in range(cases):
    case_str= "Case #"+str(i+1)+": "
    line=raw_input()
    c, f, x = line.split(" ")
    r = how_much_time(float(c), float(f), float(x), 2)
    print case_str+str(r)
