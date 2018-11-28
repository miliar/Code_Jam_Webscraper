import sys

t = int(sys.stdin.readline())

def process_layout():
    answer = int(sys.stdin.readline()) - 1
    for i in range(4):
        if (i == answer):
            line = sys.stdin.readline().strip()
        else:
            sys.stdin.readline()
    return line

for test_num in range(1, t+1):
    line_1 = process_layout()
    line_2 = process_layout()  
    intersection = [val for val in line_1.split() if val in line_2.split()]
    result = "Case #" + str(test_num) + ": "
    if len(intersection) == 0:
        result += "Volunteer cheated!"
    elif len(intersection) == 1:
        result += intersection[0]
    else:
        result += "Bad magician!"
    print(result)
    
    
