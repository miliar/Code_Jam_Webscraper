num = input()
str = ""
for x in range(1, num)
a = list(map(int, input().split()))
N = a[0]
s = a[1]
p = a[2]
t = a[3:len(a)]
m = 0;

for i in range(0, len(t)):
        if t[i] >= 0:
                if t[i]%3 == 0:
                        if t[i]//3 >= p:
                                m += 1
                        elif t[i]//3 + 1 >= p and s > 0 and t[i]//3 - 1 >= 0:
                                s -= 1
                                m += 1
                elif t[i]%3 == 1:
                        if (t[i]-1)//3 + 1 >= p:
                                m += 1
                elif t[i]%3 == 2:
                        if (t[i]-2)//3 + 1 >= p:
                                m += 1
                        elif (t[i]-2)//3 + 2 >= p and s > 0:
                                s -= 1
                                m += 1
print(m)