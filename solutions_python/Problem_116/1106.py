def main():
    T = int(raw_input())
    res = []
    for i in xrange(T):
        test_case = []
        test_case_map = []
        for j in xrange(4):
            temp = []
            test_case.append(list(raw_input()))
            if test_case[j][0] == 'X':
                temp.append(1)
            elif test_case[j][0] == 'O':
                temp.append(-1)
            elif test_case[j][0] == '.':
                temp.append(-10)
            elif test_case[j][0] == 'T':
                temp.append(0)
            if test_case[j][1] == 'X':
                temp.append(1)
            elif test_case[j][1] == 'O':
                temp.append(-1)
            elif test_case[j][1] == '.':
                temp.append(-10)
            elif test_case[j][1] == 'T':
                temp.append(0)
            if test_case[j][2] == 'X':
                temp.append(1)
            elif test_case[j][2] == 'O':
                temp.append(-1)
            elif test_case[j][2] == '.':
                temp.append(-10)
            elif test_case[j][2] == 'T':
                temp.append(0)
            if test_case[j][3] == 'X':
                temp.append(1)
            elif test_case[j][3] == 'O':
                temp.append(-1)
            elif test_case[j][3] == '.':
                temp.append(-10)
            elif test_case[j][3] == 'T':
                temp.append(0)
            test_case_map.append(temp)
        result_cases = game_result(test_case_map)
        set_draw = 0
        set_not = 0
        for k in result_cases:
            if k == 3 or k == 4:
                res.append("X won")
                set_draw = 0
                set_not = 0
                break
            elif k == -3 or k == -4:
                res.append("O won")
                set_draw = 0
                set_not = 0
                break
            elif k<3 and k>-3:
                set_draw = 1
            elif k <-4:
                set_not = 1
        if set_not == 0:
            if set_draw == 1:
                res.append("Draw")
        else:
            res.append("Game has not completed")
        if i != T-1:
            raw_input()
    for i in xrange(1,T+1):
        print "Case #%d:"%i,res[i-1]

def game_result(test_case_map):
    result_cases = []
    temp = 0
    for i in xrange(4):
        result_cases.append(sum(test_case_map[i]))
    for i in xrange(4):
        for j in xrange(4):
            temp = temp + test_case_map[j][i]
        result_cases.append(temp)
        temp = 0
    for i in xrange(4):
        temp = temp + test_case_map[i][i]
    result_cases.append(temp)
    temp = 0
    for i in xrange(4):
        temp = temp + test_case_map[i][3-i]
    result_cases.append(temp)
    temp = 0
    return result_cases
if __name__ == "__main__":
    main()
