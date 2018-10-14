import sys

def read_rows():
    rows = []
    for cur_row in range(0,4):
        rows.append([int(x) for x in sys.stdin.readline().split(" ")])
    return rows

def do_case(test):
    found = []
    first_rows = []
    second_rows = []
    first_row = int(sys.stdin.readline()) - 1
    first_rows = read_rows()
    second_row = int(sys.stdin.readline()) - 1
    second_rows = read_rows()
    for num in first_rows[first_row]:
        if num in second_rows[second_row]:
            found.append(num)

    if len(found) == 1:
        answer = found[0]
    elif len(found) > 1:
        answer = "Bad magician!"
    elif len(found) == 0:
        answer = "Volunteer cheated!"
                    
    return answer
    
        
if __name__ == "__main__":
    num_tests = int(sys.stdin.readline())

    for test in range(1, num_tests+1):
        answer = do_case(test) 
        print "Case #%s: %s" % (test, answer)
    
