LINES_FOR_EACH_INPUT = 1
INPUT_FILE_NAME = 'B-small-attempt0.in'
OUTPUT_FILE_NAME = 'B-small-attempt0.out'

def tricolor(R,B,Y):
    s=R+B+Y
    sizes=[(R,'R'),(B,'B'),(Y,'Y')]
    sizes.sort(key=lambda x: x[0])
    k=sizes[0][0]+sizes[1][0]-sizes[2][0]
    if k<0:
        return 'IMPOSSIBLE'
    temp='abc'*k+'ac'*(sizes[0][0]-k)+'bc'*(sizes[1][0]-k)
    return temp.replace('a',sizes[0][1]).replace('b',sizes[1][1]).replace('c',sizes[2][1])
def do_case(colors):
    N=colors[0]
    R=colors[1]
    O=colors[2]
    Y=colors[3]
    G=colors[4]
    B=colors[5]
    V=colors[6]
    R1=R-G
    Y1=Y-V
    B1=B-O

    if R1==0 and N==2*R:
        return 'RG'*R
    if Y1==0 and N==2*Y:
        return 'YV'*Y
    if B1==0 and N==2*B:
        return 'BO'*B
    if ((R1<=0 and G>0) or (Y1<=0 and V>0) or (B1<0 and O>0)):
        return 'IMPOSSIBLE'
    temp=tricolor(R1,B1,Y1)
    if temp=='IMPOSSIBLE':
        return temp
    return temp.replace('R','RG'*G+'R',1).replace('Y','YV'*V+'Y',1).replace('B','BO'*O+'B',1)


def do_parse(input):
    return [int(num) for num in input[0].rstrip().split(" ")]


def main():
    input_f = open(INPUT_FILE_NAME, 'r')
    output = []

    num_of_test_cases = int(input_f.readline(), 10)

    input_lines = input_f.readlines()

    for test_case in range(num_of_test_cases):
        parsed_input = do_parse(input_lines[test_case * LINES_FOR_EACH_INPUT: (test_case + 1) * LINES_FOR_EACH_INPUT])
        output.append('Case #' + str(test_case + 1) + ': ' + do_case(parsed_input))

    output_f = open(OUTPUT_FILE_NAME, 'w')
    output_f.write('\n'.join(output))

    input_f.close()
    output_f.close()


if __name__ == '__main__':
    main()
