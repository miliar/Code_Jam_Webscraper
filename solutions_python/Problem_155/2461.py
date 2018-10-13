from collections import deque
file = open("A-large.in",'r')
output = open("y.txt", 'w')

for index,line in enumerate(file):
    total = 0
    out = 0
    if (index != 0):
        st = line.split(" ")[1]
        st = st.replace("\n","")
        print(st)
        for i in range(0,len(st)):
            print("round {} total {}".format(i,total))
            while (i > total):
                out +=1
                total+=1
            total += int(st[i])

        output.write("Case #{}: {} \n".format(index,out))
