# Sean Liu
# Title

# FUNCTIONS



# IMPLEMENTATION

f = open("input.txt", "r")
g = open("output.txt", "w")

T = int(f.readline())

for i in range(T):

    line = f.readline().split()

    A = int(line[0])
    B = int(line[1])
    K = int(line[2])

    tot = 0
    
    for k in range(K):
        for a in range(A):
            for b in range(B):
                if a&b == k:
                    tot += 1

    g.write("Case #{}: {}\n".format(i+1, tot))

f.close()
g.close()
