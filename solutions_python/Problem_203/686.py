import json


class Grid:
    def __init__(self, minX, minY, maxX, maxY):
        self.minX = minX
        self.minY = minY
        self.maxX = maxX
        self.maxY = maxY

    def update(self, x, y):
        self.minX = x if self.minX > x else self.minX
        self.minY = y if self.minY > y else self.minY
        self.maxX = x if self.maxX < x else self.maxX
        self.maxY = y if self.maxY < y else self.maxY

    def __str__(self):
        return json.dumps(self.__dict__)


class AlphabetCake:

    @staticmethod
    def solve(r, c, cakes):
        debug = False
        preprocess = {}
        # 전처리를 하자 alphabet, minx, miny, maxx, maxy
        for i in range(r):
            for j in range(c):
                if cakes[i][j] == '?':
                    continue
                if cakes[i][j] not in preprocess:
                    preprocess[cakes[i][j]] = Grid(i, j, i, j)
                else:
                    grid = preprocess[cakes[i][j]]
                    grid.update(i, j)

        # 최소의 grid를 채우기
        for alphabet, grid in preprocess.items():
            for i in range(grid.minX, grid.maxX+1):
                for j in range(grid.minY, grid.maxY+1):
                    cakes[i][j] = alphabet

        if debug:
            print('#1')
            for i in range(r):
                for j in range(c):
                    print(cakes[i][j], end='')
                print("")

        # # 남은 ? 채우기
        for i in range(r):
            prev = '?'
            for j in range(c):
                if cakes[i][j] != '?':
                    prev = cakes[i][j]
                    continue
                if prev == '?':
                    continue

                # check 색칠해도 되는지(rectangular rule) 확인하고 색칠
                grid = preprocess[prev]
                if all(cakes[i2][j] == '?' for i2 in range(grid.minX, grid.maxX+1)):
                    for i2 in range(grid.minX, grid.maxX+1):
                        cakes[i2][j] = prev
                    # print('alpabet %s grid maxY chaged %s to %s' %(prev, grid.maxY, j))
                    grid.maxY = j

        if debug:
            print('#2')
            for i in range(r):
                for j in range(c):
                    print(cakes[i][j], end='')
                print("")

        for i in reversed(range(r)):
            prev = '?'
            for j in reversed(range(c)):
                if cakes[i][j] != '?':
                    prev = cakes[i][j]
                    continue

                if prev == '?':
                    continue

                # check 색칠해도 되는지(rectangular rule) 확인하고 색칠
                grid = preprocess[prev]
                if all(cakes[i2][j] == '?' for i2 in range(grid.minX, grid.maxX+1)):
                    for i2 in range(grid.minX, grid.maxX + 1):
                        cakes[i2][j] = prev
                    # print('alpabet %s grid minY chaged %s to %s' % (prev, grid.minY, j))
                    grid.minY = j

        if debug:
            print('#3')
            for i in range(r):
                for j in range(c):
                    print(cakes[i][j], end='')
                print("")

        for j in range(c):
            prev = '?'
            for i in range(r):
                if cakes[i][j] != '?':
                    prev = cakes[i][j]
                    continue

                if prev == '?':
                    continue

                # check 색칠해도 되는지(rectangular rule) 확인하고 색칠
                grid = preprocess[prev]
                if all(cakes[i][j2] == '?' for j2 in range(grid.minY, grid.minY+1)):
                    for j2 in range(grid.minY, grid.maxY+1):
                        cakes[i][j2] = prev
                    # print('alpabet %s grid maxY chaged %s to %s' %(prev, grid.maxY, j))
                    grid.maxX = i

        if debug:
            print('#4')
            for i in range(r):
                for j in range(c):
                    print(cakes[i][j], end='')
                print("")

        prev = cakes[r-1][c-1]
        for j in reversed(range(c)):
            prev = '?'
            for i in reversed(range(r)):
                if cakes[i][j] != '?':
                    prev = cakes[i][j]
                    continue

                if prev == '?':
                    continue

                # check 색칠해도 되는지(rectangular rule) 확인하고 색칠
                grid = preprocess[prev]
                if all(cakes[i][j2] == '?' for j2 in range(grid.minY, grid.maxY+1)):
                    for j2 in range(grid.minY, grid.maxY + 1):
                        cakes[i][j2] = prev
                    # print('alpabet %s grid minY chaged %s to %s' % (prev, grid.minY, j))
                    grid.minX = j

        if debug:
            print('#5')
            for i in range(r):
                for j in range(c):
                    print(cakes[i][j], end='')
                print("")
        return '\n'.join(['%s' % ''.join([cake for cake in cake_row]) for cake_row in cakes])

    @staticmethod
    def main():
        t = int(input())
        for i in range(0, t):
            r_and_c = input()
            r, c = r_and_c.split(' ')
            r, c = int(r), int(c)
            cakes = []
            for j in range(0, r):
                cake_row = list(input())
                cakes.append(cake_row)
            print('Case #%s: \n%s' % (i + 1, AlphabetCake.solve(r, c, cakes)))


if __name__ == "__main__":
    AlphabetCake.main()