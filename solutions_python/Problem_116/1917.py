# Google Code Jam 2013 Qualification round, Tic-tac-toe
import sys

if(len(sys.argv) > 1):
    f = open(sys.argv[1])
else:
    f = open("simple.txt")

res_ref = {'X' : 'X won',
        'O' : 'O won',
        'D' : 'Draw',
        'N' : 'Game has not completed'
        }

def check_diag(square):
    check = []
    i = 0
    for row in square:
        check.append(row[i])
        i += 1
    

    print(check)
    if not check_row(check):
        check = []
        i = 3
        for row in square:
            check.append(row[i])
            i -= 1

    return check_row(check)

def check_row(row):
    elem = None
    for item in row:
        if not item == 'T' and not item == '.':
            elem = item
            break;

    if not elem:
        return None

    for item in row:
        if not item == elem and not item == 'T':
            return None

    return elem

def check_rows(square):
    for row in square:
        check = check_row(row)
        if check:
            return check


    return None

def find_dot(square):
    for row in square:
        for item in row:
            if item == '.':
                return True

    return False

def check_status(string):
    result = []
    ncases = int(string[0])
    string = string[1:]

    for i in range(ncases):
        arr_hoz = []
        arr_vert = [[] for a in range(4)]
        for j in range(4):
            arr_hoz.append([a for a in string[0]])
            for k in range(4):
                arr_vert[k].append(arr_hoz[j][k])
            string = string[1:]

        string = string[1:]
        check = check_rows(arr_hoz)
        if check:
            result.append((i+1, check))
            continue

        check = check_rows(arr_vert)
        if check:
            result.append((i+1, check))
            continue
        
        check = check_diag(arr_hoz)
        if check:
            result.append((i+1, check))
            continue

        if find_dot(arr_hoz):
            result.append((i+1, 'N'))
            continue

        result.append((i+1, 'D'))

    return result


def print_output(result):
    output = open("output_tic", "w")
    for (num, res) in result:
        output.write("Case #{}: {}\n".format(num, res_ref[res]))
        
lines = f.read().splitlines()
print_output(check_status(lines))
    

