def solve():
    row, column = map(int, input.readline().split())
    answer = list()
    for i in range(row):
        tmp = input.readline().split()[0]
        answer.append([_ for _ in tmp])

    while True:
        flag = False
        for i in range(row):
            cur_char = None
            need = 0
            for j in range(column):
                ch = answer[i][j]
                if ch == '?':
                    flag = True
                    if cur_char:
                        answer[i][j] = cur_char
                    else:
                        need += 1
                else:
                    cur_char = ch
                    for _ in range(need+1):
                        answer[i][j-_] = cur_char
                    need = 0
        if not flag:
            return '\n'.join([''.join(_) for _ in answer]) # нужен нормальный вывод ответа


        for j in range(column):
            cur_char = None
            need = 0
            for i in range(row):
                ch = answer[i][j]
                if ch == '?':
                    flag = True
                    if cur_char:
                        answer[i][j] = cur_char
                    else:
                        need += 1
                else:
                    cur_char = ch
                    for _ in range(need+1):
                        answer[i-_][j] = cur_char
                    need = 0
        if not flag:
            return '\n'.join([''.join(_) for _ in answer]) # нужен нормальный вывод ответа


input = open('in.txt', 'r')
output = open('out.txt', 'w')
t = int(input.readline())
for test_case in range(t):
    output.write('Case #{}:\n{}\n'.format(test_case + 1, solve()))