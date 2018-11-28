__author__ = 'Mohit'

filename = "C://Temp/B-large.in"
ins = open(filename, "r")
array = []
for line in ins:
    array.append(line)

for i in range(1,len(array)):
    numbers=array[i].split(" ")
    C=float(numbers[0])
    F=float(numbers[1])
    X=float(numbers[2])

    cookies=2.0
    res=0
    while(X/cookies>(C/cookies)+(X/(cookies+F))):
        res=res+(C/cookies)
        cookies=cookies+F
    res += X / cookies
    res = "{0:.7f}".format(res)
    string = 'Case #%d: %s' % (i, res)
    print string