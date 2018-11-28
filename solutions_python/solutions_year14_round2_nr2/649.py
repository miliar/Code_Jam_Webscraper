def generate_number(a,b,k):
    count = 0
    for i in range(a):
        for j in range(b):
            if(i&j)<k:
               count += 1
    return count


f = open("B-small-attempt0.in")
f1 = open("output.txt","w")
s = f.readline()
test_case = int(s)


for i in range(test_case):
    s = f.readline()
    temp = s.split(" ")
    A = int(temp[0])
    B = int(temp[1])
    K = int(temp[2])
    n = generate_number(A,B,K)
    f1.write("Case #"+str(i+1)+": "+str(n)+"\n")

f.close()
f1.close()
    
    
