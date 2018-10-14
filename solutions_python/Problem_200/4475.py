lines = list(tuple(open("B-large.in", 'r')))
num = int(lines.pop(0).strip("\n"))
numbers = []
for line in lines:
    numbers.append(line.strip("\n"))


file = open("B-large-attempt0.out", "w")
for i in range(num):
    temp = numbers[i]
    l = len(temp)
    j = l-1
    while j > 0:
        do = 0
        while int(temp[j]) < int(temp[j-1]) or int(temp[j]) == 0 and int(temp[j-1])==0:
            temp = '%0*d' % (l, int(temp) - 10**(l-(j+1)))
            do = 1
        if do == 1:
            for k in range(j+1,l,1):
                t = list(temp)
                t[k] = "9"
                temp=''.join(t)
        j -= 1
    temp = str(int(temp))
    file.write("Case #"+str(i+1)+": " + str(temp)+"\n")
