import sys
filein, fileout = sys.argv[1:3]

def moves(line):
    n, *rest = line.split()
    move_list = [(rest[2*i],int(rest[2*i+1])) for i in range(int(n))]
    while move_list:
        move = move_list.pop(0)
        other = [x for x in move_list if x[0] != move[0]]
        other_next = other[0] if other else None
        yield move, other_next

def solve(line):
    pos, time = {'O': 1, 'B': 1}, 0
    for move, other in moves(line):
        diff = abs(move[1]-pos[move[0]])+1
        time += diff
        if other:
            pos[other[0]] += min(diff, abs(other[1]-pos[other[0]])) * (1 if other[1] > pos[other[0]] else -1)
        pos[move[0]] = move[1]
    return time

if __name__ == '__main__':
    with open(filein, 'rU') as f1, open(fileout, 'w') as f2:
        T = int(f1.readline())
        for case in range(T):
            f2.write("Case #{}: {}\n".format(case+1, solve(f1.readline().strip())))

