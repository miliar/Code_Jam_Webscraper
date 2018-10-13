in_file = open('B-small-attempt0.in','r')
out_file = open('Bout.txt','w')
n = int(in_file.readline())

for i in range(n):
    num = 0
    giv=list(map(int,in_file.readline().split()))
    for j in range(giv[0]):
        for k in range(giv[1]):
            s = j & k
            if s < giv[2]:
                num = num + 1
    out_file.write("Case #" + str(i+1) +": "+ str(num) +"\n")





out_file.close()
in_file.close()
