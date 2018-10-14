def action(i, b, j):
    count = 0
    while(i < b):
        temp = reverse(i);
        while(temp != i):
            if(temp > i and temp <= b):
                count = count + 1
                temp = reverse(temp)
            else:
                    if(temp == i or temp == i/10 or temp == i/100):
                        break
                    else: temp = reverse(temp)
        i = i +1
    fw.write("Case #" + str(j) + ": " + str(count) +'\n')
    print "done"
    
def reverse(y):
    x = 0;
    if(y/10 == 0):
        return y
    if(y/100 == 0):
        if(y%10 == 0):
            return y
        x = y%10
        y = y/10
        y = y + x*10;
        return y
    if(y/1000 == 0):
        if(y%10 == 0):
            return (y%100) * 10+(y/100);
        x = y%10
        y = y/10
        y = y + x*100;
        return y

count =0
j=0
fr = open("in.txt" , 'r')
fw = open("out.txt", 'w')
for line in fr:
    if j>0:
        k=line.split(" ")
        a=k[0]
        b=k[1]
        i = a
        action(int(i),int(b),j)
    j=j+1


