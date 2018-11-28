t = int(input())
for i in range(1, t + 1):
    n = input()
    found = False
    while not found:
        found = True
        for j in range(1, len(n)):
            if int(n[j]) < int(n[j - 1]):
                found = False
                n = str(int(n) - 1)
                break
    print("Case #" + str(i) + ": " + n)
print ("END")