import sys

def solve(ropes):
    result = 0
    for i in range(len(ropes)):
        for j in range(i+1, len(ropes)):
            if (ropes[i][0] < ropes[j][0] and ropes[i][1] > ropes[j][1]):
                result += 1
            elif (ropes[i][0] > ropes[j][0] and ropes[i][1] < ropes[j][1]):
                result += 1
    return result


def main():
    input = open(sys.argv[1])
    t = int(input.next())

    for i in range(t):
        n = int(input.next())
        ropes = []
        for j in range(n):
            rope = [int(a) for a in input.next().split()]
            ropes.append(rope)
        
        print "Case #%d: %d" % (i + 1, solve(ropes))
        

main()
        

                