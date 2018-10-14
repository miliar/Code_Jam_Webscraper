def add_name(grid):
    for i, row in enumerate(grid):
        j = 0
        while j < len(row):
            if row[j] != '?':
                c = row[j]
                while j > 0 and row[j-1] == '?':
                    row[j-1] = c
                    j-=1
                while j < len(row) - 1 and row[j+1] == '?':
                    row[j+1] = c
                    j+=1
            j+=1
    i = 0
    while i < len(grid):
        if grid[i][0] == '?':
            if i == 0:
                j = 1
                while grid[j][0] == '?':
                    j+=1
                grid[i] = list(grid[j])
            else:
                grid[i] = list(grid[i-1])
        i+=1

def main():
    with open('/Users/tengg/Downloads/A-large.in') as f:
        t = int(f.readline())
        for i in range(1, t+1):
            r, c = map(int, f.readline().split(' '))
            grid = []
            for _ in range(r):
                grid.append(list(f.readline().strip('\n')))
            add_name(grid)
            print(f"Case #{i}:")
            for row in grid:
                print(''.join(row))

if __name__ == '__main__':
    main()
