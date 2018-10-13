def solve(answer1, cards1, answer2, cards2):
    solution = set(cards1[answer1 - 1]) & set(cards2[answer2 - 1])
    count = len(solution)
    if count > 0:
        if count == 1:
            return min(solution)
        return 'Bad magician!'
    return 'Volunteer cheated!'

def main():
    T = int(raw_input())
    for t in range(T):
        answer1 = int(raw_input())
        cards1 = [[int(x) for x in raw_input().split(' ')] for i in range(4)]
        answer2 = int(raw_input())
        cards2 = [[int(x) for x in raw_input().split(' ')] for i in range(4)]
        solution = solve(answer1, cards1, answer2, cards2)
        print 'Case #%d: %s' % (t+1, solution)

main()
