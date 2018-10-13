fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
n = int(fin.readline())
for i in range(1, n + 1):
    c, f, x = map(float, fin.readline().split())
    ans = x / 2
    farms = 1
    matrix = [[0, 2]]
    while matrix[-1][0] < ans:
        time, cook = matrix[-1][0] + c / matrix[-1][1], matrix[-1][1] + f
        matrix.append([time, cook])
        ans = min(ans, matrix[-1][0] + x / matrix[-1][1])
    print('Case #' + str(i) + ':', ans, file = fout)
fin.close()
fout.close()