import sys

message_template = "Case #{x}: {y}"

def main():
    with open(sys.argv[1]) as input_file:
        tests = int(input_file.readline())

        test_num = 0
        for testcase in input_file:
            test_num += 1
            x, r, c = (int(x) for x in testcase.strip().split())

            #print('r: {r}, c: {c}, x: {x}'.format(x=x, r=r, c=c))

            if (r*c)%x != 0:
                # board dimensions
                winner = "RICHARD"
            elif x>max(r, c):
                # richard makes a really long 1*x piece
                winner = "RICHARD"
            elif (x+1)//2 > min(r, c):
                # check for 'L' shaped ominos
                winner = "RICHARD"
            elif x>3 and 2 in (r,c):
                # weird edge case
                winner = "RICHARD"
            else:
                winner = "GABRIEL"

            print(message_template.format(x=test_num, y=winner))

if __name__ == '__main__':
    main()
