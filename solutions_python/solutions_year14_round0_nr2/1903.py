with open ("B-large.in", "r") as myfile:
    problem=myfile.read()
lines = problem.split('\n')
cases = int(lines[0])
for i in range(cases):
    line = lines[i+1].split(' ')
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])
    CookieperSecond = 2
    time = 0
    while(True):
        NextStep = c / CookieperSecond
        time += NextStep
        if ( NextStep >=  x / CookieperSecond ):
            time = x / CookieperSecond
            break
        elif ( ((x - c) / CookieperSecond ) <= (x/(CookieperSecond+f)) ):
            time += (x - c) / CookieperSecond
            break
        else:
            CookieperSecond += f
    time = round(time,7)
    print("Case #"+str(i+1)+": "+str(time))
