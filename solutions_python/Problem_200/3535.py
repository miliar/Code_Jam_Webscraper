t = int(input())

def count(numberIn):
    num = numberIn
    while True:
        number = map(int, str(num))
        number = list(number)
        success = True
        for i in range(0, len(number) - 1):
            if number[i] > number[i + 1]:
                success = False
        if success == True:
            return num
        num -= 1
    return 0
for i in range(1, t + 1):
  n = int(input())
  n = count(n)
  print("Case #{}: {}".format(i, n))
