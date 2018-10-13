

def nextv(l1, l2, minus):
    cm = minus
    if l1 == '1' and l2 == '1': v = '1'
    if l1 == '1' and l2 == 'i': v = 'i'
    if l1 == '1' and l2 == 'j': v = 'j'
    if l1 == '1' and l2 == 'k': v = 'k'

    if l1 == 'i' and l2 == '1': v = 'i'
    if l1 == 'i' and l2 == 'i': v = '1'; cm = not cm
    if l1 == 'i' and l2 == 'j': v = 'k'
    if l1 == 'i' and l2 == 'k': v = 'j'; cm = not cm

    if l1 == 'j' and l2 == '1': v = 'j'
    if l1 == 'j' and l2 == 'i': v = 'k'; cm = not cm
    if l1 == 'j' and l2 == 'j': v = '1'; cm = not cm
    if l1 == 'j' and l2 == 'k': v = 'i'

    if l1 == 'k' and l2 == '1': v = 'k'
    if l1 == 'k' and l2 == 'i': v = 'j'
    if l1 == 'k' and l2 == 'j': v = 'i'; cm = not cm
    if l1 == 'k' and l2 == 'k': v = '1'; cm = not cm
    #print("V %c + %c (%d) -> %c (%d)" % (l1, l2, minus, v, cm))
    return v, cm


testcases = int(input())

for t in range(testcases):
    nums, x = list(map(int, input().split()))
    letters = input()
    letters = letters * x

    left = -1
    right = -1

    if len(letters) < 3:
        print("Case #%d: NO" % (t+1,))
        continue

    current = '1'
    minus = False
    for i in range(len(letters)):
        current, minus = nextv(current, letters[i], minus)
        if current == 'i' and minus is False:
            left = i + 1
            break

    current = '1'
    minus = False
    for i in range(len(letters)-1, 0, -1):
        current, minus = nextv(letters[i], current, minus)
        if current == 'k' and minus is False:
            right = i
            break

    result = "NO"
    if left != -1 and right != -1 and left < right:
        current = '1'
        minus = False
        for i in range(left, right):
            current, minus = nextv(current, letters[i], minus)
        if current == 'j' and minus is False:
            result = "YES"

    print("Case #%d: %s" % (t+1, result))
