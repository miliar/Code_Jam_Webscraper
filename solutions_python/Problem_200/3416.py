def broke(temp):    
    for i in range(len(temp)-1):
        #print (temp)
        if (temp[i] >  temp[i+1]):
            temp[i] = abs(temp[i] - 1)
            temp[i+1:] = [9] * (len(temp)-(i+1))

    if (sorted(temp) == temp):
        return int(''.join(map(str,temp)))
    else:
        return broke(temp)

x = input()
cases = []
for i in range(x):
    cases.append(input())

for x in range(len(cases)):
    t = str(cases[x])
    if len(t) == 1:
        print ("Case #" + str(x+1) + ": " + str(cases[x]))
        continue
    temp = []
    for i in range(len(t)):
        temp.append(int(t[i]))
    print ("Case #" + str(x+1) + ": " + str(broke(temp)))
