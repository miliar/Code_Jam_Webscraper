f = open("B-large.in","r")
data = []
for line in f:
    data.append(line.strip())
f.close()
for i in range(1,len(data)):
    string = data[i]
    for j in range(len(string)-1,0,-1):
        if int(string[j])<int(string[j-1]):
            head = str(int(string[:j])-1)
            if head == "0":
                head = ""
            string = head + "9"*(len(string)-j)
    print("Case #"+str(i)+": "+string)
