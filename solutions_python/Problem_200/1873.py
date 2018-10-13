file = open("B-large.in","r")
lines = file.readlines()[1:]
file.close()
temp = []
results = []

def trim(num):
    num = str(num)
    for d in range(len(num)-1):
        if num[d]>num[d+1]:
            num = num[:d]+str(int(num[d])-1)+(len(num)-d-1)*"9"
    return int(num)

def isTidy(num):
    num = str(num)
    curr = num[0]
    for char in num:
        if char<curr:
            return False
        curr = char
    return True

for i in lines:
    i = int(i)
    while not isTidy(i):
        i = trim(i)
        if isTidy(i):
            break
        i-=1
    temp.append(i)

file = open("B-large.out","w")
for i in range(len(temp)):
    results.append("Case #{0}: {1}\n".format(i+1,temp[i]))
file.writelines(results)
file.close()

