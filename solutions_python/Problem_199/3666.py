from sys import argv

def solution(order, k):
    correct = [True] * len(order)
    order_bool = [True if i == '+' else False for i in order]

    flip_count = 0

    index = 0
    while correct != order_bool:
        if index+k > len(order_bool): return 'IMPOSSIBLE'
        if not order_bool[index]:
            order_bool[index:index+k] = [not o for o in order_bool[index:index+k]]
            flip_count+=1
        index +=1
    return flip_count


def main():
    filename = './pan_in_small.txt'
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        T = int( f.readline() )
        case_count = 0
        for i in xrange(T):
            case_count += 1
            d = f.readline().rstrip('\n')
            order,k = d.split(' ')
            ans = solution(order, int(k))
            print "Case #" + str(case_count) + ": " + str(ans)

main()
