# -*- coding: utf-8 -*-

T = int(raw_input())
for case in xrange(1, T + 1):
    data = raw_input().split(' ')
    N = int(data[0])
    data = data[1:]
    data = [(data[i * 2], int(data[i * 2 + 1])) for i in xrange(N)]

    # 次にOrangeとBlueが押すべきボタンを記録しておく
    orange = []
    blue = []
    target = {'O': orange, 'B': blue}
    for color, pos in data:
        target[color].append(pos)

    # ボタンを順番に押していく
    sec = 0
    pos_orange = 1
    pos_blue = 1
    for color, pos in data:
        if color == 'O':
            t = abs(pos - pos_orange) + 1
            sec += t
            if blue:
                if pos_blue < blue[0]:
                    pos_blue = min(pos_blue + t, blue[0])
                else:
                    pos_blue = max(pos_blue - t, blue[0])
            pos_orange = orange.pop(0)
        else:
            t = abs(pos - pos_blue) + 1
            sec += t
            if orange:
                if pos_orange < orange[0]:
                    pos_orange = min(pos_orange + t, orange[0])
                else:
                    pos_orange = max(pos_orange - t, orange[0])
            pos_blue = blue.pop(0)
    print 'Case #%d: %d' % (case, sec)

