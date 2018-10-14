
def get_row():
    rownumber = int(raw_input())
    rows = []
    for _ in range(4): rows.append(raw_input())
    return set([int(x) for x in rows[rownumber - 1].split(" ")])

def solvecase(case_number):
    ret = "Case #%d: " % case_number
    r1, r2 = get_row(), get_row()
    intersect = [x for x in r1 if x in r2]
    if len(intersect) == 1:
        ret += str(intersect[0])
    elif len(intersect):
        ret += "Bad magician!"
    else: ret += "Volunteer cheated!"
    print ret
    
def main():
    case_amount = int(raw_input())
    for casen in range(1, case_amount + 1): solvecase(casen)

if __name__ == "__main__": main()
