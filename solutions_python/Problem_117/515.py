# Each cell must be higher every other cell in it's row OR in it's line


# Tells if i is greater than or equal to everything else in the list
def is_majoring(i, l):
    for e in l:
        if e > i:
            return False
    return True


def solve(mown, N, M):
    rotated = list(zip(*mown))

    for y in range(N):
        for x in range(M):
            if not(is_majoring(mown[y][x], mown[y]) or is_majoring(rotated[x][y], rotated[x])):
                return False
    return True


if __name__ == "__main__":
    for i in range(int(input())):
        N, M = map(int, input().split())
        mown = []
        for y in range(N):
            mown.append(list(map(int, input().split())))

        if solve(mown, N, M):
            print("Case #" + str(i+1) + ": " + "YES")
        else:
            print("Case #" + str(i+1) + ": " + "NO")
