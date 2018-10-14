"""
Given a set of pancakes, calculate the minimum number of flips
to turn them all over, but you can only flip K pancakes in 
a row at any given time
"""

def process(pancakes, k):
    flips = 0
    for i in range(len(pancakes) - (k-1)):
        if pancakes[i] == '-':
            pancakes = pancakes[:i] + flip(pancakes[i:i+k]) + pancakes[i+k:]
            flips += 1

    success = True
    for p in pancakes:
        if p == '-':
            success = False

    return flips if success else 'IMPOSSIBLE'

def flip(pancakes):
    result = ''
    for i in range(len(pancakes)):
        if pancakes[i] == '-':
            result += '+'
        else:
            result += '-'
    return result


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    pancakes, k = input().split(' ')
    print('Case #{}: {}'.format(i, process(pancakes, int(k))))
