# Standing Ovation

PLAYER1 = "RICHARD"
PLAYER2 = "GABRIEL"

def omino(x, r, c):
    if (c * r) % x != 0:
        return PLAYER1
    if x == 1:
        return PLAYER2
    if x == 2:
        return PLAYER2
    if x == 3:
        if (r % x == 0 and c >= 2) or (c % x == 0 and r >= 2):
            return PLAYER2
        else:
            return PLAYER1
    if x == 4:
        if (r % x == 0 and c >= 3) or (c % x == 0 and r >= 3):
            return PLAYER2
        if (r % x == 0 and c < 3) or (c % x == 0 and r < 3):
            return PLAYER1
        if (r % x == 2) and (c % x == 2):
            if r == 2 or c == 2:
                return PLAYER1
            else:
                return PLAYER2
                
args = {};

with open('d:\input.txt', 'rt') as in_file:
    line_count = int(in_file.readline())
    for i in range(1, line_count+1):
        line = in_file.readline()
        str_args = line.split()
        x = int(str_args[0])
        r = int(str_args[1])
        c = int(str_args[2])
        args[i] = {'x': x, 'r': r, 'c': c}
        
answer = {}
for item in args.items():
    key = item[0]
    value = item[1]
    answer[key] = omino(**value)

with open('d:\output.txt', 'wt') as out_file:
    for item in answer.items():
        test_num = item[0]
        test_answer = item[1]
        print("Case #%d: %s" % (test_num, test_answer), file=out_file)