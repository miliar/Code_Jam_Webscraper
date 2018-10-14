for n in range(int(raw_input())):
    strr = raw_input()
    a = True
    flag = 0
    for i in range(len(strr)):
        if i<len(strr)-1 and int(strr[i]) > int(strr[i+1]):

            if i >= 1:
                if int(strr[flag]) == int(strr[i]):
                    result = strr[0:flag] + str(int(strr[flag])-1)
                    for j in range(flag,len(strr) - 1):
                        result = result + '9'
                        a = False
                else:
                    result = strr[0:i] + str(int(strr[i])-1)
                    for j in range(i,len(strr) - 1):
                        result = result + '9'
                        a = False
            elif i < 1:
                if int(strr[flag]) == int(strr[i]):
                    result = str(int(strr[flag]) - 1)
                    for j in range(flag,len(strr) - 1):
                        result = result + '9'
                        a = False
                else:
                    result = str(int(strr[i]) - 1)
                    for j in range(i,len(strr) - 1):
                        result = result + '9'
                        a = False

        elif i<len(strr)-1 and int(strr[i]) == int(strr[i+1]):
            if  int(strr[flag]) != int(strr[i]):
                flag = i
        if not a:
            break

    if a:
        print "Case #"+ str(n+1) + ": " + strr
    else:
        print "Case #"+ str(n+1) + ": " + str(int(result))