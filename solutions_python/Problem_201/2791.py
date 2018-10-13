fp = open('C-small-1-attempt1.in')

tc_line = fp.readline()

T = int(tc_line)

for testcase in range(T):
    line = fp.readline()
    data = line.split()
    N = int(data[0]) + 2
    K = int(data[1])
    bathroom = ""
    for i in range(N):
        if i == N - 1 or i == 0:
            bathroom += "*"
        else:
            bathroom += "."

    for p in range(K):
        ls = []
        rs = []
        minlrs = []
        maxlrs = []
        maxn1 = 0
        count1 = 0
        maxn2 = 0
        count2 = 0
        lastindex = -1
        for i in range(len(bathroom)):
            if bathroom[i] == '*':
                ls.append(0)
                rs.append(0)
                minlrs.append(0)
            else:
                tls = 0
                trs = 0
                j = i
                while j >= 0:
                    j -= 1
                    if(bathroom[j] == '.'):
                        tls += 1
                    elif(bathroom[j] == '*'):
                        ls.append(tls)
                        break
                j = i
                while j < N:
                    j += 1
                    if(bathroom[j] == '.'):
                        trs += 1
                    elif(bathroom[j] == '*'):
                        rs.append(trs)
                        break
                num1 = min(ls[i], rs[i])

                if(num1 == maxn1):
                    count1 += 1
                if(num1 > maxn1):
                    count1 = 1
                    maxn1 = num1
                minlrs.append(num1)

        for i in range(len(minlrs)):
            if minlrs[i] == maxn1:
                num2 = max(ls[i], rs[i])
                if (num2 == maxn2):
                    count2 += 1
                if (num2 > maxn2):
                    count2 = 1
                    maxn2 = num2
                maxlrs.append(num2)
            else:
                maxlrs.append(0)
        for i in range(len(minlrs)):
            if count1 == 1 and minlrs[i] == maxn1:
                lastindex = i
                bathroom = bathroom[:i] + '*' + bathroom[i + 1:]
                break
            elif count1 > 1 and count2 == 1 and maxlrs[i] == maxn2:
                lastindex = i
                bathroom = bathroom[:i] + '*' + bathroom[i + 1:]
                break
            elif count1 > 1 and count2 > 1 and maxlrs[i] == maxn2 and maxlrs[i] == maxn2:
                lastindex = i
                bathroom = bathroom[:i] + '*' + bathroom[i+1:]
                break
    # print(bathroom)
    print("Case #" + str(testcase+1) + ": " + str(maxlrs[lastindex]) + " " + str(minlrs[lastindex]))


