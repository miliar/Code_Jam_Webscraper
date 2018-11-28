#!/usr/bin/env python3

FILE = "A-small-input.in"
results = {0: "Volunteer cheated!",
        2: "Bad magician!"}

def gen():
    with open(FILE) as f:
        for case in range(1, int(f.readline()) + 1):
            answer = int(f.readline())
            cards = [list(map(int, f.readline().split())) for i in range(4)]
            answer2 = int(f.readline())
            cards2 = [list(map(int, f.readline().split())) for i in range(4)]
            yield case, answer, cards, answer2, cards2


with open("magictrickoutput.txt", "w") as out:
    for case, answer1, cards1, answer2, cards2 in gen():
        possibles = cards1[answer1-1]
        possibles2 = cards2[answer2-1]
        matches = [x for x in possibles if x in possibles2]
        lenmatches = len(matches)
        result = ""
        if lenmatches is 0:
            result = results[0]
        elif lenmatches >= 2:
            result = results[2]
        else:
            result = str(matches[0])
        print("Case #{0}: {1}".format(case, result), file=out)
        
