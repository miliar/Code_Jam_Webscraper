def intersect(w1, w2):
    a1, b1 = w1
    a2, b2 = w2
    return (a1 > a2 and b2 > b1) or (a2 > a1 and b1 > b2)

def solve(n, wires):
    count = 0
    for i in range(n-1):
        for j in range(i, n):
            if intersect(wires[i], wires[j]):
                count += 1
    return count

def split(line):
    return chomp(line).split(' ')

def chomp(line):
    return line.replace('\n', '')

if __name__ == '__main__':

    input_problem = 'A'
    input_set = 'large'#-attempt0'
    in_file = open('{}-{}.in'.format(input_problem, input_set), 'r')
    out_file = open('{}-{}.out'.format(input_problem, input_set), 'w')

    line = in_file.readline()

    count = int(line)
    for i in range(1, count+1):
        print(i, 'of', count)
        n = int(chomp(in_file.readline()))
        wires = []
        for j in range(n):
            wires.append(tuple([int(x) for x in split(in_file.readline())]))
        out_file.write('Case #{}: {}\n'.format(i, solve(n, wires)))

    in_file.close()
    out_file.close()

