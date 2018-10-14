
def checkuni(data):
    up = True
    for i in range(1, len(data)):
        if up and data[i]<data[i-1]:
            up = False
        if not up and data[i]>data[i-1]:
            return False
    return True


infile = open("B-large.in", "r")
outfile = open("Bout.txt", "w")



total=0
t = int(infile.readline().rstrip())
for z in range(1, t+1):
    n = infile.readline()
    data = infile.readline().split()
    data = [int(i) for i in data]
    smallest = -1
    cleared = 0
    solution=0
    left = 0
    right = len(data)-1
    while True:
        if cleared==len(data):
            break
        curr = 10**15
        for i in range(0, len(data)):
            if data[i]<curr and data[i]>smallest:
                curr = data[i]
                pos=i
        smallest = curr
        #print(curr, pos, data)
        if pos-left < abs(pos-right):
            i=pos
            while i>0:
                data[i], data[i-1] = data[i-1], data[i]
                i-=1
            solution+=pos-left
            left+=1
        else:
            for i in range(pos, right):
                data[i], data[i+1] = data[i+1], data[i]
            solution+=abs(pos-right)
            right-=1
        if checkuni(data):
            break
        cleared+=1

    output = "Case #"+str(z)+": "+str(solution)+"\n"
    print(output)
    outfile.write(output)

infile.close()
outfile.close()
