import sys

def read_answer():
    answer = []
    answer_row = int(sys.stdin.readline().strip())
    for row_number in xrange(0, 4):
        row = sys.stdin.readline().strip()
        if row_number + 1 == answer_row:
            answer = list(map(int, row.split(' ')))
    return answer


def solve():
    t = int(sys.stdin.readline().strip())
    for test_case in xrange(0, t):
        answer_1 = read_answer()
        answer_2 = read_answer()
        answer = set(answer_1).intersection(set(answer_2))
        result = ""
        if len(answer) == 1:
            result = str(answer.pop())
        elif len(answer) > 1:
            result = "Bad magician!"
        elif len(answer) == 0:
            result = "Volunteer cheated!"

        print >> sys.stdout, "Case #%s: %s" % (test_case + 1, result)

if __name__ == "__main__":
    solve()