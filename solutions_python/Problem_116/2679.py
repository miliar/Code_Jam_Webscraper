
def main():
    f = open('input.txt', 'r')
    read_data = f.read()

    process(read_data)

    # print solve([ ['X', 'X', 'X', 'T'], ['.', '.', '.', '.'], ['O', 'O', '.', '.'], ['.', '.', '.', '.'] ])

def process(data):

    rows = data.split('\n')
    
    i = 0
    map = []

    for row in rows:
        
        if i%5 != 0:
            map.append(list(row))
        elif (i%5 == 0) and (i > 0):
            print 'Case #' + str(i/5) + ': ' + solve(map)

            map = []
        i += 1

def solve(map):
    v = []
    results = []
    result = ''

    for i in range(0, 4):
        result = check_items([map[i][0], map[i][1], map[i][2], map[i][3]])
        results.append(result)        
        if (result == 'x') or (result == 'o'):
            break

        result = check_items([map[0][i], map[1][i], map[2][i], map[3][i]])
        results.append(result)        
        if (result == 'x') or (result == 'o'):
            break

    if (result != 'x') and (result != 'o'):
        result = check_items([map[0][0], map[1][1], map[2][2], map[3][3]])
        results.append(result)        
    
    if (result != 'x') and (result != 'o'):
        result = check_items([map[3][0], map[2][1], map[1][2], map[0][3]])
        results.append(result)        


    if result == 'x':
        return 'X won'
    elif result == 'o':
        return 'O won'
    elif '?' in results:
        return 'Game has not completed'
    else:
        return 'Draw'

def check_items(q):
    
    result = '?'

    if ('X' in q) and ('O' in q):
        result = 'z'
    elif is_x(q[0]) and is_x(q[1]) and is_x(q[2]) and is_x(q[3]):
        result = 'x'
    elif is_o(q[0]) and is_o(q[1]) and is_o(q[2]) and is_o(q[3]):
        result = 'o'

    return result

def is_x(i):
    return i == 'X' or i == 'T'

def is_o(i):
    return i == 'O' or i == 'T'    

main()