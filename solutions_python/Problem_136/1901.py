with open ("data.txt", "r") as file:
    data=file.read()
lines = data.split('\n')
cases = int(lines[0])
for i in range(cases):
    case = lines[i+1].split(' ')
    c = float(case[0])
    f = float(case[1])
    x = float(case[2])
    CookieSecond = 2
    time = 0
    while (1==1):
        NextStep = c / CookieSecond
        time += NextStep
        if ( NextStep >=  x / CookieSecond ):
            time = x / CookieSecond
            break
        elif ( ((x - c) / CookieSecond ) <= (x/(CookieSecond+f)) ):
            time += (x - c) / CookieSecond
            break
        else:
            CookieSecond += f
    time = round(time,7)
    print("Case #"+str(i+1)+": "+str(time))
