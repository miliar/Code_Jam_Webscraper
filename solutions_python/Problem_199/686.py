def readint(): return int(raw_input())
def readarray(x): return map(x, raw_input().split())

def toInt(nums):
    y = []
    for x in nums:
        x = int(x)
        y.append(x)
    return y

cases = readint()
for case in range(cases):

    pancakes_string, size_of_flip = raw_input().split()
    size_of_flip = int(size_of_flip)
    pancakes = list(pancakes_string)

    flips = 0
    for i, pancake in enumerate(pancakes):
        if pancakes.count('-') > 0:
            if pancake == '-':
                if i > len(pancakes) - size_of_flip:
                    break
                for j in range(i, i+size_of_flip):
                    if pancakes[j] == '-':
                        pancakes[j] = '+'
                    else:
                        pancakes[j] = '-'
                flips += 1
                #print 'flip',flips,pancakes
    if pancakes.count('-') > 0: flips = "IMPOSSIBLE"

    print 'Case #%i:'%(case+1), flips
