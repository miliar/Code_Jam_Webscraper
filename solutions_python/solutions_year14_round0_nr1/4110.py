import sys

def magic_trick(in_file):
    test_cases = int(in_file.readline().rstrip())

    for _, num in enumerate(range(test_cases)):
        row1 = int(in_file.readline().rstrip())
        cards1 = []
        for _ in range(4):
            cards1.append(in_file.readline().rstrip().split())

        row2 = int(in_file.readline().rstrip())
        cards2 = []
        for _ in range(4):
            cards2.append(in_file.readline().rstrip().split())

        output = 'Case #{}: '.format(num+1)
        union = cards1[row1-1]+cards2[row2-1]
        overlap = set(union)
        if len(overlap) == len(union):
            print output + 'Volunteer cheated!'
        elif len(overlap) < len(union)-1:
            print output + "Bad magician!"
        else:
            for x in overlap:
                if union.count(x)>1:
                    print output+x
                    break

if __name__ == '__main__':
    with open(sys.argv[1]) as in_file:
        magic_trick(in_file)
