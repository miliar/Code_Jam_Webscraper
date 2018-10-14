def cal(a, b):
    sign = ""
    c = ""
    if (len(a) == 2):
        a = a[1]
        sign = "-"
    if (a == "1"):
        c = b
    elif (a == "i"):
        if (b == "1"): c = "i"
        elif (b == "i"): c = "-1"
        elif (b == "j"): c = "k"
        elif (b == "k"): c = "-j"
    elif (a == "j"):
        if (b == "1"): c = "j"
        elif (b == "i"): c = "-k"
        elif (b == "j"): c = "-1"
        elif (b == "k"): c = "i"
    elif (a == "k"):
        if (b == "1"): c = "k"
        elif (b == "i"): c = "j"
        elif (b == "j"): c = "-i"
        elif (b == "k"): c = "-1"
    if (len(c) == 2 and len(sign) == 1):
        sign = ""
        c = c[1]
    return sign + c

with open("C-small-attempt2.in","r") as f:
    numOfCase = int(f.readline())
    print(numOfCase)
    for i in range(numOfCase):
        ans = "NO"
        currentStander = 0
        lines = f.readline().split()
        maxChar = int(lines[0])
        num = int(lines[1])
        listString = f.readline().split()
        string = ""
        flag = "i"
        currentChar = "1"
        for j in range(num):
            string += listString[0]
        for k in range(len(string)):
            if (flag == "i"):
                currentChar = cal(currentChar,string[k])
                if (currentChar == "i"):
                    flag = "j"
                    currentChar = "1"
            elif (flag == "j"):
                currentChar = cal(currentChar,string[k])
                if (currentChar == "j"):
                    flag = "k"
                    currentChar = "1"
            elif (flag == "k"):
                currentChar = cal(currentChar,string[k])
        if (flag == "k" and "k" == currentChar):
            ans = "YES"
        print("Case #%d: %s" % (i+1,ans))
f.closed















