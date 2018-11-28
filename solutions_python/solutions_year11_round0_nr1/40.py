import sys

def get_line():
    return sys.stdin.readline().strip()

def read_nums():
    return [int(item) for item in get_line().split(" ")]

def solve( buttons ):
    o_left = o_right = 1
    b_left = b_right = 1
    sec = 0
    for (color, pos) in buttons:
        if color=='O':
            move = max(0, o_left - pos, pos - o_right )
            o_left = o_right = pos
            b_left -= move + 1
            b_right += move + 1
        elif color=='B':
            move = max(0, b_left - pos, pos - b_right )
            b_left = b_right = pos
            o_left -= move + 1
            o_right += move + 1
        else:
            raise Warning, "unkonwn color"
        sec += move + 1
    return sec

(T,) = read_nums()
for test in range(1, T+1):
    test_case = get_line().split(" ")
    N = int(test_case[0])
    buttons = []
    for i in range(N):
        color = test_case[1+i*2]
        pos = int(test_case[1+i*2+1])
        buttons.append( (color, pos) )
    sec = solve( buttons )

    print "Case #%d: %d" % (test, sec)
