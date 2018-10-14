
def solver(moves):
    for i in range(len(moves)):
        moves[i].append(i)
    blues = [[move[0], int(move[1]), move[2]] for move in moves if move[0] == 'B']
    # print blues
    oranges = [[move[0], int(move[1]), move[2]] for move in moves if move[0] == 'O']
    # print oranges
    tick = 0
    blue_pos = 1
    orange_pos = 1
    while len(blues) > 0 or len(oranges) > 0:
        # print 'blues ', blues
        # print 'oranges ', oranges
        tick += 1
        # check for index out of range
        if len(blues) > 0 and len(oranges) > 0:
            target = blues[0][2] < oranges[0][2] and 'B' or 'O'
        elif len(blues) > 0:
            target = 'B'
        elif len(oranges) > 0:
            target = 'O'
        # print 'target', target
        if target == 'B':
            if blue_pos == blues[0][1]:
                # pressing button so pop the top element
                blues.pop(0)
            else:
                if blue_pos < blues[0][1]:
                    blue_pos += 1
                elif blue_pos > blues[0][1]:
                    blue_pos -= 1
            if len(oranges) > 0:
                if orange_pos == oranges[0][1]:
                    pass
                elif orange_pos < oranges[0][1]:
                    orange_pos += 1
                elif orange_pos > oranges[0][1]:
                    orange_pos -= 1
        elif target == 'O':
            if orange_pos == oranges[0][1]:
                # pressing button so pop the top element
                oranges.pop(0)
            else:
                if orange_pos < oranges[0][1]:
                    orange_pos += 1
                elif orange_pos > oranges[0][1]:
                    orange_pos -= 1
            if len(blues) > 0:
                if blue_pos == blues[0][1]:
                    pass
                elif blue_pos < blues[0][1]:
                    blue_pos += 1
                elif blue_pos > blues[0][1]:
                    blue_pos -= 1
    return tick



def ssi(s):
    """
    space separated integers
    """
    return map(int, s.strip('\n').split())

def main():
    # open input file
    input_file = open('infile.txt')
    cases = int(input_file.readline())
    output = []
    # loop through cases passing input to solver
    for c in range(cases):
        print c
        l = input_file.readline().strip().split()
        num_pushes = int(l.pop(0))
        moves = []
        for n in range(num_pushes):
            moves.append(l[n*2:n*2+2])
        # print moves
        answer = solver(moves)
        output.append('Case #%d: %d\n' % (c+1, answer))
    input_file.close()
    # open output file
    output_file = open('outfile.txt', 'w')
    # write ouput to file
    output_file.writelines(output)
    # close out file
    output_file.close()
    print 'Done!'



if __name__=='__main__':
    main()
