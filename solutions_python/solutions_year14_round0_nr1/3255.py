"""
16 cards on square grid
4 rows of cards with 4 cards in each row

Each card has different number 1 to 16 written on side that is showing

magiican asks volunteer to choose a card and tell row that it is in

then arrange the cards into a square grid again, possibly different order
tell which row again
magician correctly determines which row

"""

def nextline(f):
    line = f.readline().strip()
    if not line:
        line = f.readline().strip()
        if not line:
            return "XXXX"
        return line
    return line

def parse_input():
    with open("data.in") as f:
        cases = []
        nextline(f)
        while True:
            line = nextline(f)
            if line == "XXXX":
                return cases
            first_answer = int(line)
            first_row_set = [map(int, nextline(f).split(" ")),
                             map(int, nextline(f).split(" ")),
                             map(int, nextline(f).split(" ")),
                             map(int, nextline(f).split(" "))]
            second_answer = int(nextline(f))
            second_row_set = [map(int, nextline(f).split(" ")),
                              map(int, nextline(f).split(" ")),
                              map(int, nextline(f).split(" ")),
                              map(int, nextline(f).split(" "))]
            cases.append([first_answer, first_row_set,
                          second_answer, second_row_set])

def output(case, result):
    with open("data.out", "a") as f:
        if result is True: # mulitple answers
            text = "Bad magician!"
        elif result is False: # no correct answer
            text = "Volunteer cheated!"
        else:
            text = str(result) # numeric answer
        f.write("Case #" + str(case) + ": " + text + "\n")
        

def get_result(case):
    first_answer, first_row_set, second_answer, second_row_set = case
    
    first_row = first_answer - 1
    second_row = second_answer - 1

    first_possible = set(first_row_set[first_row])
    second_possible = set(second_row_set[second_row])

    result = first_possible.intersection(second_possible)

    if len(result) == 1:
        return result.pop()
    elif len(result) == 0:
        return False
    else:
        return True
    

def main():
    cases = parse_input()
    for i, case in enumerate(cases):
        result = get_result(case)
        output(i + 1, result)


if __name__ == "__main__":
    main()
