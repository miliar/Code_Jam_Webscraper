import sys

def main():
    num_cases = int(sys.stdin.readline())

    i = 0
    while i < num_cases:
        idx = int(sys.stdin.readline()) - 1  
        j = 0

        while j < 4:
            line = sys.stdin.readline()

            if j == idx:
                first = set(map(int, line.strip().split(' ')))

            j += 1

        idx = int(sys.stdin.readline()) - 1
        j = 0

        while j < 4:
            line = sys.stdin.readline()

            if j == idx:
                second = set(map(int, line.strip().split(' ')))

            j += 1

        cards = first.intersection(second)

        if len(cards) == 0:
            result = "Volunteer cheated!"
        elif len(cards) > 1:
            result = "Bad magician!"
        else:
            result = "%d" % (cards.pop())

        print "Case #%d: %s" % (i+1, result)
        

        i += 1

main()
