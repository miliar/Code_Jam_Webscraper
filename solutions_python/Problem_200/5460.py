def isTidy(num):
    return sorted(str(num)) == list(str(num))

def tidify(num):
    num = int(num)
    while not isTidy(num):
        num -= 1
    return num

count = int(input())
for i in range(count):
    case = input()
    print("Case #" + str(i+1) + ": " + str(tidify(case)))
