#! /bin/python
rows = [[i*4+j for j in xrange(4)] for i in xrange(4)]
cols = [[i*4+j for i in xrange(4)] for j in xrange(4)]
digonals = [[i*4+i for i in xrange(4)], [i*4-i+3 for i in xrange(4)]]

all_lines = rows + cols + digonals

def judge(board):
    for line in all_lines:
        first = board[line[0]]
        if first == '.':
            continue
        elif first == 'T':
            first = board[line[1]]
            if first == '.':
                continue
        win = first + 'T'
        if board[line[1]] in win and board[line[2]] in win and board[line[3]] in win:
            return first + ' won'
    if '.' in board:
        return "Game has not completed"
    else:
        return "Draw"
    
def main():
    import sys
    lines = [l.strip() for l in open(sys.argv[1])]
    for i in range(1, len(lines), 5):
        print "Case #%d: %s" % (1+(i-1)/5, judge(''.join(lines[i:i+4])))
main()
