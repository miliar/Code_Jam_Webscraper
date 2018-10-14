input = open("b.in" , "r")
output = open("b.out" , "w")

T = int(input.readline())

for k in range(1, T + 1):
    A, B, K = map(int, input.readline().split(" "))
    c = 0
    for i in range(A):
        for j in range(B):
            if i & j < K:
                c += 1
    print c
    output.write("Case #" + str(k) + ": " + str(c) + "\n")

input.close()
output.close()
