def check(num):
    n = str(num)
    for i in range(len(n)-1):
        if(int(n[i+1])<int(n[i])):
            return False
    return True

file = open("B-small-attempt1.in", "r")
out = open("b-small.out","w")
t = int(file.readline())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(file.readline())
    while(not check(n)):
        n = n-1
    out.write("Case #{}: {}\n".format(i, n))

