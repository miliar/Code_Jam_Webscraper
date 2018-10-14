import sys

# How many cases?
def main():
    T = int(sys.stdin.readline())
    for case in range(1,T+1):
        loop(case)


def loop(case):
    result = []
    
    # Process and sort the first 16 cards
    row1 = int(sys.stdin.readline()) - 1
    inp = []
    for i in range(0,4):
        inptemp = sys.stdin.readline().split(' ')
        inptemp = [int(x) for x in inptemp]
        inp.append(inptemp)
    row1 = inp[row1]
    
    # Process and sort the second 16 cards
    row2 = int(sys.stdin.readline()) - 1
    inp = []
    for i in range(0,4):
        inptemp = sys.stdin.readline().split(' ')
        inptemp = [int(x) for x in inptemp]
        inp.append(inptemp)
    row2 = inp[row2]
    
    # Check how which number(s) match on the 2 rows from the 2 card sets
    for num in row1:
        if num in row2:
            result.append(num)
    
    # Determine output message
    if result:
        if len(result) == 1:
            out = str(result[0])
        else:
            out = "Bad Magician!"
    else:
        out = "Volunteer Cheated!"
    
    # Print output message
    sys.stdout.write("Case #{}: {}\n".format(case, out))

if __name__ == '__main__':
    main()