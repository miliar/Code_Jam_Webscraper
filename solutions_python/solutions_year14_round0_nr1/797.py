def getRow(sel_idx):
    rows = []
    for _ in range(4):
        input_arr = raw_input().split(" ")
        rows.append(set(input_arr))
    return rows[sel_idx]

test_cnt = input()
output = []
for num in range(0, test_cnt):
    first = getRow(input() - 1)
    second = getRow(input() - 1)
    common_elms = first.intersection(second)
    answer = ""
    if len(common_elms) == 1:
        answer = common_elms.pop()
    elif len(common_elms) > 1:   
        answer = "Bad magician!"
    elif len(common_elms) == 0:
        answer = "Volunteer cheated!"
    output.append("Case #%d: %s" % ((num + 1), answer))
    
for v in output:
    print v

