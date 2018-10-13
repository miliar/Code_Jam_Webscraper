import math
import sys
import getopt

def get_arguments():
    in_file= "/home/se/Downloads/A-small.in"
    out_file ="/home/se/Downloads/test.out"
    opts, args = getopt.getopt(sys.argv[1:], "i:o:")
    for o, a in opts:
        print o
        if o in ("-i"):
            in_file = a;
        elif o in ("-o"):
            out_file = a;
    print(in_file, out_file)
    return (in_file, out_file)

def run(in_file, out_file):
    input = open(in_file)
    output = open(out_file, "w")

    line = input.readline().strip()
    print line
    cases = int(line)

    for case in range(0,cases):
        first_answer = int(input.readline().strip())
        first_cards = load_cards(input)
        second_answer = int(input.readline().strip())
        second_cards = load_cards(input)

        answer = analyse_trick(first_answer, first_cards, second_answer, second_cards)

        print >> output, "Case #%d: %s" % (case+1, answer)
        print "Case #%d: %s" % (case+1, answer)

def load_cards(input):
    cards = []
    for i in range(0,4):
        values = input.readline().strip().split(' ')
        cards.append(values)
    return cards

def analyse_trick(answer_one, cards_one, answer_two, cards_two):
    possible_answers_one = cards_one[answer_one-1]
    print possible_answers_one
    possible_answers_two = cards_two[answer_two-1]
    print possible_answers_two
    possible_answers = []
    for a in possible_answers_one:
        for b in possible_answers_two:
            if a == b:
                possible_answers.append(a)
    num_answers = len(possible_answers)
    if num_answers == 1:
        return possible_answers[0]
    elif num_answers > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"
    return "1"

def main():
    (in_file, out_file) = get_arguments()
    run(in_file, out_file)

main()

