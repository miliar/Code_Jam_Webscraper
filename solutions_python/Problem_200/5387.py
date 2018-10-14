def func(strIn):  # takes in a string
    for b in range(1, len(strIn)):
        if strIn[b] < strIn[b - 1]:
            intIn = int(strIn)
            intIn -= 1
            strIn = str(intIn)
            return func(strIn)
    return strIn

t = int(input())

a = []
for i in range(1, t + 1):
     a.append(input())
nu = []
for gg in a:
    nu.append(func(gg))

for i in range(1, t + 1):
    print("Case #" + str(i) +': '+nu[i-1])




