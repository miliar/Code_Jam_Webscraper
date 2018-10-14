from operator import itemgetter
from math import ceil

def int_input():
    return int(raw_input())

def list_str_input():
    return raw_input().split()

def list_int_input():
    return map(int, list_str_input())

def list_char_input():
    return list(raw_input())

def table_int_input(h):
    return [list_int_input() for i in range(h)]

def table_char_input(h):
    return [list_char_input() for i in range(h)]

def get_moves(num_moves, seq, min_time):
    moves = []
    len_seq = len(seq)
    total_dist = 0
    for i in range(num_moves):
        dist = seq[i%len_seq]
        boostable = min(dist, max(0, total_dist+dist-(min_time/2)))
        unboostable = dist-boostable
        moves.append((total_dist, dist, boostable))
        total_dist += dist
    moves.sort(key=itemgetter(2), reverse=True)
    return moves

def get_time(moves, l):
    time = 0
    for move in moves:
        if l > 0 and move[2] > 0:
            l -= 1
            time += move[2]+((move[1]-move[2])*2)
        else:
            time += move[1]*2
    return time

def solve(case):
    line = list_int_input()
    l = line[0]
    t = line[1]
    n = line[2]
    c = line[3]
    clist = line[4:]
    moves = get_moves(n, clist, t)
    time = get_time(moves, l) 
    print 'Case #%d: %d' % (case, time)

def main():
    for c in range(int_input()):
        solve(c+1)

main()

