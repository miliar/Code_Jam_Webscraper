import sys
f = open('./input', 'r')
t = int(f.readline())

for test in range(0, t):
    f.readline()
    s = f.readline().split()

    s1 =  []
    for i in range (0, len(s)):
        temp = int(s[i])
        s1.append(temp)

    result = s1[0]
    for i in range(1, len(s1)):
        result = result^s1[i]
    sum = 0
    for i in range (0, len(s1)):
        sum = sum + s1[i]
    sys.stdout.write("Case #" +str(test + 1)+ ': ' )
    if result != 0:
        print 'NO'
    else:
        print (sum - min(s1))


