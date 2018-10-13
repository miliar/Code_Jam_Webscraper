import math

T = input()

results = []
for t in range(T):
    A, B = raw_input().split()
    A = int(A)
    B = int(B)
    a = int(math.ceil(A**.5))
    b = int(math.floor(B**.5))

    counter = 0
    for n in range(a, b + 1):
        if str(n) == str(n)[::-1]:
            if str(n**2) == str(n**2)[::-1]:
                counter += 1

    results.append(counter)
    
for i in range(len(results)):
    print "Case #" + str(i + 1) + ": " + str(results[i])
