FILE = 'A-large.in'
OUT = 'out.txt'

def bake(cake):
    cake_map = []
    bad = []

    for i in range(len(cake)):
        cake_map.append([])
        
        for j in range(len(cake[i])):
            cake_map[i].append(cake[i][j])

    for row in cake_map:
        bad = ['?']*len(row)
        
        while '?' in row and row != ['?']*len(row):
            #print(row)
            c = '?'

            for letter in row:
                if letter != '?':
                    c = letter

                    idx = row.index(c)
                    left = idx
                    right = idx

                    while left-1 >= 0 and row[left-1] == '?':
                        row[left-1] = c
                        left -= 1

                    while right+1 < len(row) and row[right+1] == '?':
                        row[right+1] = c
                        right += 1

    while not full(cake_map):
        for i in range(len(cake_map)):
            if cake_map[i] == bad:
                if i-1 >= 0 and cake_map[i-1] != bad:
                    cake_map[i] = cake_map[i-1]

                elif i+1 < len(cake_map) and cake_map[i+1] != bad:
                    cake_map[i] = cake_map[i+1]

    return cake_map

def full(cake):
    for row in cake:
        if row == ['?']*len(row):
            return False

    return True

def main():
    file = open(FILE)
    out = open(OUT, 'w')
    lines = file.readlines()

    i = 1
    case = 1

    while i < len(lines):
        line = lines[i].strip().split()

        rows = int(line[0])

        cake = []

        for line in lines[i+1:i+1+rows]:
            cake.append(line.strip())

        baked = bake(cake)

        out.write('Case #{}:\n'.format(case))

        for row in baked:
            out.write(''.join(row)+'\n')

        i += rows+1
        case += 1

    out.close()

main()
