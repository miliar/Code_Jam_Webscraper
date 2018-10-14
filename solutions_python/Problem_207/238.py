#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# vi: set fileencoding=utf-8 :


def solve(N, R, O, Y, G, B, V):
    unicorn = {'R': R, 'O': O, 'Y': Y, 'G': G, 'B': B, 'V': V}
    stall = []
    max_color = 0
    max_number = 0
    for color in unicorn:
        if unicorn[color] > max_number:
            max_number = unicorn[color]
            max_color = color
    stall.append(max_color)
    unicorn[max_color] -= 1
    for i in range(1, N):
        max_color = 0
        max_number = 0
        for color in unicorn:
            if color == stall[-1]:
                continue
            if unicorn[color] > max_number or unicorn[color] >= max_number and color == stall[0]:
                max_number = unicorn[color]
                max_color = color
        if max_color == 0:
            return 'IMPOSSIBLE'
        stall.append(max_color)
        unicorn[max_color] -= 1
    if stall[0] == stall[-1]:
        return 'IMPOSSIBLE'
    return ''.join(stall)


def answer(input_file_name):
    input_file = open(input_file_name)
    T = int(input_file.readline())
    for case_number in range(1, T + 1):
        N, R, O, Y, G, B, V = map(int, input_file.readline().split())
        print('Case #%d: %s' % (case_number, solve(N, R, O, Y, G, B, V)))
    return


if __name__=='__main__':
    import sys
    answer(sys.argv[1])
