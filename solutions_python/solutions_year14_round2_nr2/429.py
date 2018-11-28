def solve(numbers):
    global case
    global wfile
    case += 1
    
    A = numbers[0]
    B = numbers[1]
    K = numbers[2]
    
    print(A, B, K)
    
    n = 0
    for a in range(A):
        for b in range(B):
            if a & b < K:
                n += 1
    print(n)
    wfile.write("Case #{0}: {1}\n".format(case, n))


f = open("input.in")
f.readline()

wfile = open("output.out", "w")

case = 0

line = f.readline()
while line != "":
    numbers = line.split(" ")
    numbers = [int(i) for i in numbers]

    solve(numbers)

    line = f.readline()
