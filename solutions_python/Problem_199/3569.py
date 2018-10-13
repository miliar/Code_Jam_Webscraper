def solve(row, flipper):
    #print(trim(row), flipper)
    steps = 0;
    
    if is_good(row):
        return steps
    
    row = trim(row)

    while len(row) >= flipper:        
        for i in range(flipper):
            #print(i, row[i])
            if row[i] == '-':
                row[i] = '+'
            else:
                row[i] = '-'

        steps = steps + 1
        
        if is_good(row):
            return steps
        
        row = trim(row)
            
    return 'IMPOSSIBLE'

def is_good(row):
    return '-' not in row

def trim(row):
    start = row.index('-')

    return row[start:]


input = open('A-large.in', 'r')
output = open('A-large.out', 'w')

cases = int(input.readline())


for i in range(1, cases+1):
    (row, flipper) = input.readline().split(' ')
    #print('Case #{}: {}'.format(i, solve(list(row), int(flipper))))
    output.write('Case #{}: {}\n'.format(i, solve(list(row), int(flipper))))


input.close()
output.close()
