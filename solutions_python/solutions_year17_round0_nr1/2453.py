## flips k symbols in a list starting at position pos
def flip(myList, pos, k):
    for p, ch in enumerate(myList[pos:pos+k], pos):
        if ch == '+':
            myList[p] = '-'
        else:
            myList[p] = '+'


## verifies that str is ok starting from position pos until the end
def is_strOk(myList, pos):
    for ch in myList[pos:]:
        if ch == '-':
            return False
    return True


t = int(input())
for i in range(1, t+1):
    case_str, k = input().split(' ')
    case = list(case_str)
    k = int(k)
    stop_n = len(case_str) - k
    flippings = 0
    for pos, ch in enumerate(case_str):
        if case[pos] == '+':
            continue
        elif pos <= stop_n:
            flip(case, pos, k)
            flippings += 1
        else:
            if not is_strOk(case, stop_n):
                flippings = 'IMPOSSIBLE'
            break
    print("Case #{}: {}".format(i, flippings))
