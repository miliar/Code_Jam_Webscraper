import sys

N = int(sys.stdin.readline())

for i in range(N):
    s = []
    for j in range(4):
        s.append(sys.stdin.readline().strip())
    sys.stdin.readline()
    flag = ''
    is_com = "yes"
    for j in range(4):
        for k in range(4):
            if s[j][k] == '.':
                is_com = "no"
    for j in range(4):
        if      (s[j][0] == s[j][1] or s[j][0] == 'T' or s[j][1] == 'T') \
            and (s[j][0] == s[j][2] or s[j][0] == 'T' or s[j][2] == 'T') \
            and (s[j][0] == s[j][3] or s[j][0] == 'T' or s[j][3] == 'T') \
            and (s[j][1] == s[j][2] or s[j][1] == 'T' or s[j][2] == 'T') \
            and (s[j][1] == s[j][3] or s[j][1] == 'T' or s[j][3] == 'T') \
            and (s[j][2] == s[j][3] or s[j][2] == 'T' or s[j][3] == 'T') \
            and s[j][0] != '.' \
            and s[j][1] != '.' \
            and s[j][2] != '.' \
            and s[j][3] != '.':
                if s[j][0] != 'T':
                    flag = s[j][1]
                else:
                    flag = s[1][j]
        if      (s[0][j] == s[1][j] or s[0][j] == 'T' or s[1][j] == 'T') \
            and (s[0][j] == s[2][j] or s[0][j] == 'T' or s[2][j] == 'T') \
            and (s[0][j] == s[3][j] or s[0][j] == 'T' or s[3][j] == 'T') \
            and (s[1][j] == s[2][j] or s[1][j] == 'T' or s[2][j] == 'T') \
            and (s[1][j] == s[3][j] or s[1][j] == 'T' or s[3][j] == 'T') \
            and (s[2][j] == s[3][j] or s[2][j] == 'T' or s[3][j] == 'T') \
            and s[0][j] != '.' \
            and s[1][j] != '.' \
            and s[2][j] != '.' \
            and s[3][j] != '.':
                if s[0][j] != 'T':
                    flag = s[0][j]
                else:
                    flag = s[1][j]
    if      (s[0][0] == s[1][1] or s[0][0] == 'T' or s[1][1] == 'T') \
        and (s[0][0] == s[2][2] or s[0][0] == 'T' or s[2][2] == 'T') \
        and (s[0][0] == s[3][3] or s[0][0] == 'T' or s[3][3] == 'T') \
        and (s[1][1] == s[2][2] or s[1][1] == 'T' or s[2][2] == 'T') \
        and (s[1][1] == s[3][3] or s[1][1] == 'T' or s[3][3] == 'T') \
        and (s[2][2] == s[3][3] or s[2][2] == 'T' or s[3][3] == 'T') \
        and s[0][0] != '.' \
        and s[1][1] != '.' \
        and s[2][2] != '.' \
        and s[3][3] != '.':
            if s[0][0] != 'T':
                flag = s[0][0]
            else:
                flag = s[1][1]
    if      (s[0][3] == s[1][2] or s[0][3] == 'T' or s[1][2] == 'T') \
        and (s[0][3] == s[2][1] or s[0][3] == 'T' or s[2][1] == 'T') \
        and (s[0][3] == s[3][0] or s[0][3] == 'T' or s[3][0] == 'T') \
        and (s[1][2] == s[2][1] or s[1][2] == 'T' or s[2][1] == 'T') \
        and (s[1][2] == s[3][0] or s[1][2] == 'T' or s[3][0] == 'T') \
        and (s[2][1] == s[3][0] or s[2][1] == 'T' or s[3][0] == 'T') \
        and s[0][3] != '.' \
        and s[1][2] != '.' \
        and s[2][1] != '.' \
        and s[3][0] != '.':
            if s[0][3] != 'T':
                flag = s[0][3]
            else:
                flag = s[1][2]
    if flag == 'X' or flag == 'O':
        print "Case #" + str(i+1) + ": " + flag + " won"
    elif flag == '' and is_com == 'no':
        print "Case #" + str(i+1) + ": Game has not completed"
    else:
        print "Case #" + str(i+1) + ": Draw"

