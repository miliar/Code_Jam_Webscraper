def mow(lawn):
    height = len(lawn)
    width = len(lawn[0])
    for i, row in enumerate(lawn):
        high = max(row)
        for j, cell in enumerate(row):
            if cell < high:
                for y in range(height):
                    if lawn[y][j] > cell:
                        return False
    return True


def get_lawn():
    dimensions = input().split(' ')
    height = int(dimensions[0])
    width = int(dimensions[1])
    lawn = []
    for i in range(height):
        row = list(map(int, input().split(' ')))
        lawn.append(row)
    return lawn


cases = int(input())
for i in range(1, cases+1):
    lawn = get_lawn()
    if mow(lawn):
        print("Case #" + str(i) + ":", "YES")
    else:
        print("Case #" + str(i) + ":", "NO")

