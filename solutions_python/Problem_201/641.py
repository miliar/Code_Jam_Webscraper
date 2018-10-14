LINES_FOR_EACH_INPUT = 1
INPUT_FILE_NAME = 'C-large.in'
OUTPUT_FILE_NAME = 'C-large.out'
def addmerge(l,n,k):
    if l:
        if(l[-1][0]==n):
            l[-1]=(n,l[-1][1]+k)
            return
    l.append((n,k))
def dists(n):
    return str(n/2)+' '+str((n-1)/2)
def stalls(n,k):
    gaps=[(n,1)]
    while k>gaps[0][1]:
        temp=gaps.pop(0)
        addmerge(gaps,temp[0]/2,temp[1])
        addmerge(gaps,(temp[0]-1)/2,temp[1])
        k-=temp[1]
    return dists(gaps[0][0])
def do_case(parsed_input):
    return stalls(int(parsed_input[0]),int(parsed_input[1]))


def do_parse(input):
    return [line.rstrip().split(" ") for line in input][0]


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