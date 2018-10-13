
def get(data,x,y):
    X = len(data[0])
    Y = len(data)
    if x < 0 or y < 0 or x >= X or y >= Y:
        return "."
    return data[y][x]

def get_and_set(data, x, y, dx, dy, size,initial):
    collision = False
    for i in range(0,size+1):
        tx = x + dx * i
        ty = y + dy * i
        if get(data,tx,ty) not in ["?",initial,initial.lower()]:
            collision = True
    if not collision:
        for i in range(0,size+1):
            tx = x + dx * i
            ty = y + dy * i
            data[ty][tx] = initial.lower()
    return collision

def solve(data):
    X = len(data[0])
    Y = len(data)
    letters = set()
    # expand each letter one by one...
    for y in range(Y):
        for x in range(X):
            initial = data[y][x]
            if initial == "?":
                continue
            if initial.lower() == initial:
                continue

            letters.add(initial)

            left = 0
            right = 0
            up = 0
            down = 0

            while not get_and_set(data, x, y, -1, 0, left+1, initial):
                left += 1
            while not get_and_set(data, x, y, +1, 0, right+1, initial):
                right += 1
            while not get_and_set(data, x - left, y - up - 1 , +1, 0, left + right, initial):
                up += 1
            while not get_and_set(data, x - left, y + down + 1, +1, 0, left + right, initial):
                down += 1

            #print(initial,up,down,left,right)

    test = ""

    for y in range(Y):
        print(("".join(data[y])).upper())
        test += ("".join(data[y]).upper())

    if "?" in test:
        print("*****************************ERROR!")
    for letter in letters:
        if letter not in test:
            print("*****************************MISSING",letter)



T = int(input())
for t in range(T):
    Y,X = [int(i) for i in input().split()]
    data = []
    for y in range(Y):
        data.append(list(input()))
    print("Case #{0}:".format(t+1))
    solve(data)