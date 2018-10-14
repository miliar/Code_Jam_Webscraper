
def process(f):
    i = iter(open(f))
    T = int(next(i).strip())
    
    with open("output", "w") as output:
        for case in range(1, T+1):
            first_row = int(next(i).strip())
            first_guess = set([map(int, next(i).strip().split()) for _ in range(4)][first_row - 1])
            
            second_row = int(next(i).strip())
            second_guess = set([map(int, next(i).strip().split()) for _ in range(4)][second_row - 1])

            possibilities = first_guess & second_guess
            print first_row, first_guess, second_row, second_guess, possibilities
            if len(possibilities) > 1:
                y = "Bad magician!"
            elif len(possibilities) == 1:
                y ,= possibilities
            else:
                y = "Volunteer cheated!"

            output.write("Case #{case}: {y}\n".format(**locals()))
            

if __name__ == "__main__":
    process("input")
