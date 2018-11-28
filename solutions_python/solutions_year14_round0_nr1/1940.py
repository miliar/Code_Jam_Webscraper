__author__ = 'ezequieldariogambaccini'


def magic_trick(answers, first_sort, second_sort):
    cheat = "Volunteer cheated!"
    bad_mage = "Bad magician!"

    first_row = first_sort[answers[0]]
    second_row = second_sort[answers[1]]
    intersection = first_row.intersection(second_row)
    if len(intersection) == 0:
        return cheat
    elif len(intersection) > 1:
        return bad_mage
    else:
        return str(intersection.pop())



def SolveMagicTrick(in_file, out_file):
    with open(out_file, "w") as out_data:
        with open(in_file, "r") as in_data:
            N = int(in_data.readline())
            for x in xrange(N):
                first_answer = int(in_data.readline())
                first_sort = [set(map(int, in_data.readline().split())) for _ in xrange(4)]
                second_answer = int(in_data.readline())
                answers = (first_answer-1, second_answer-1)
                second_sort = [set(map(int, in_data.readline().split())) for _ in xrange(4)]


                r = "Case #%d: %s\n"%(x+1,magic_trick(answers, first_sort, second_sort))

                out_data.write(r)
                print(r)

if __name__ == "__main__":
    SolveMagicTrick("A-small-attempt0.in", "out_small.txt")
