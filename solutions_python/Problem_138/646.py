#!/usr/bin/python
#! - * - encoding: utf-8 - * -

def get_input():
    return map(lambda x: float(x), raw_input().split())
def compare(item1, item2):
    if (item1) < (item2):
        return 1
    elif (item1) > (item2):
        return -1
    else:
        return 0
def start():
    N = int(raw_input())
    data, data2 = get_input(), get_input()
    data.sort()
    data2.sort(cmp=compare)
    left, right = 0, N-1
    stack ,score, score2 = 0, 0, 0
    while stack != N:
        if data[right] > data2[stack]:
            right -= 1
            stack += 1
            score += 1
        else:
            left += 1
            stack += 1
    stack, score2, left = 0, 0, 0
    data2 = data2[::-1]
    data = data[::-1]
    right = N-1
    while stack != N:
        if data2[right] > data[stack]:
            right -= 1
            stack += 1
        else:
            left += 1
            stack += 1
            score2 += 1
            
    return [score, score2]
if __name__ == "__main__":
    tc = int(raw_input())
    for i in range(tc):
        output = start()
        print "Case #%d: %d %d" % (i+1, output[0], output[1]) 
