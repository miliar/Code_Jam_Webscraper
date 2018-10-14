# Solve:
def solve(input):
    # initial
    number = list(input)
    order = tidy(number)

    # iteration
    while order != -1:
        number[order] = str(int(number[order])-1)
        for i in range(order+1,len(number)):
            number[i] = '9'
        order = tidy(number)

    while number[0] == '0':
        number.pop(0)
    return ''.join(number)



   
def tidy(noList):
    for i in range(len(noList)-1):
        if noList[i+1]<noList[i]:
            return i
    return -1

# Input:
T = int(input())
for i in range(1, T + 1):
    print("Case #{}: {} ".format(i, solve((input()))))