#Problem Solution
def solve(input):
    data = input.split(" ")
    pancakes = list(data[0])
    flipper = int(data[1])
    flips = 0
    for position in range(len(pancakes)-(flipper-1)):
        if(pancakes[position]=='-'):
            for i in range(position,position+flipper):
                if pancakes[i]=='-':
                    pancakes[i] = '+'
                else:
                    pancakes[i] = '-'
            flips+=1
    for pancake in pancakes:
        if pancake == '-':
            return 'IMPOSSIBLE'
    return flips

T = int(input())  # reads in number of test cases

# Take input
for i in range(1, T + 1):
    print("Case #{}: {} ".format(i, solve((input()))))