with open ("input.in", "r") as file:
    data=file.read()
line_data = data.split('\n')
num = int(line_data[0])
for i in range(num):
    InnerData = line_data[i+1].split(' ')
    c = float(InnerData[0])
    f = float(InnerData[1])
    x = float(InnerData[2])
    CookieperSecond = 2
    time = 0
    while ( True ):
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
