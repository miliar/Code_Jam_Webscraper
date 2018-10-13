def check(n):
    count = 0
    m = n
    while (n != 0):
        n = int(n/10)
        count += 1
    temp = 10
    for i in range(0, count):
        comp = int(m % 10)
        if (temp < comp):
            return False
        temp = int(comp)
        m = int(m/10)
    return True

def main():
    numCases = int(input());
    for test in range (1, numCases+1):
        n = [int(s) for s in input().split(" ")]
        number = n[0]
        for x in range(number, 0, -1):
            if check(x):
                print("Case #" + str(test) + ": " + str(x))
                break
main()