def run(case_num):
    r, c = [int(x) for x in input().strip().split()]
    cake = [[letter for letter in input()] for row in range(r)]
    for row in cake:
        last = row[0]
        for i in range(1, len(row)):
            if row[i] == '?' and last != '?':
                row[i] = last
            else:
                last = row[i]
        last = row[-1]
        for i in reversed(range(len(row)-1)):
            if row[i] == '?' and last != '?':
                row[i] = last
            else:
                last = row[i]
    for col_num in range(c):
        last = cake[0][col_num]
        for i in range(1, len(cake)):
            if cake[i][col_num] == '?' and last != '?':
                cake[i][col_num] = last
            else:
                last = cake[i][col_num]
        last = cake[-1][col_num]
        for i in reversed(range(len(cake)-1)):
            if cake[i][col_num] == '?' and last != '?':
                cake[i][col_num] = last
            else:
                last = cake[i][col_num]
    print("Case #{}:".format(case_num))
    for row in cake:
        print(*row, sep='')

for case in range(int(input())):
    run(case+1)
