def decrement(n, i):
    if int(n[i]) > 0:
        n[i] = str(int(n[i]) - 1)
    elif int(n[i]) == 0:
        n[i] = "9"
        decrement(n, i - 1)
    return n

def check_tidy(n):
    for i in range (0,len(n) - 1):
        if n[i] > n[i+1]:
            return False
    return True

t = input()
for i in range(0, int(t)):
    n = input()
    n = list(n)
#    n = decrement(n, len(n) - 1)
    while not check_tidy(n):
        for j in range(len(n) - 1, 0, -1):
            if n[j] < n[j-1]:
                n[j:] = ["9"] * (len(n) - j)
                decrement(n, j - 1)
    n = "".join(n)
    n = str(int(n))
    print("Case #" + str(i + 1) + ": " + n)
