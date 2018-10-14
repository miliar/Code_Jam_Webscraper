def isTidy(n):
    return list(str(n)) == sorted(str(n))

def findTidy(n):
    while isTidy(n) == False:
        if(n % 10 == 0):
            n -= 1
            continue
        number = str(n)
        exp = 0
        for digit in range(len(number) - 1):
            if number[digit] > number[digit+1]:
                    exp = digit
                    break
        number = number[:digit+1] + ("0" * (len(number) - exp - 1))
        n = int(number)
    return n


n = int(input())
for i in range(n):
    number = int(input())
    print("Case #" + str(i+1) + ": " + str(findTidy(number)))
