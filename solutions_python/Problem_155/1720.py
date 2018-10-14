f = open("in.txt", 'r')
w = open("out.txt", 'w')
for i in range(int(f.readline())):
    line = f.readline()
    strs = line.split()
    standing = int(strs[1][0])
    friends = 0
    for shyness in range(1, int(strs[0]) + 1):
        while shyness > standing:
            friends+=1
            standing+=1
        standing += int(strs[1][shyness])
    w.write("Case #"+ str(i+1) + ": " + str(friends)+'\n') 
f.close()
w.close()
