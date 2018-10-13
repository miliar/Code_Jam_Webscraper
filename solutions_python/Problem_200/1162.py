def last_tidy(sequence):
    index = len(sequence) - 1
    while index > 0:
        if sequence[index] < sequence[index-1]:
            return last_tidy(str(int(substract_one(sequence[:index]) + to_nines(sequence[index:]))))
        index -= 1
    return sequence

def substract_one(seq):
    return str(int(seq)-1)

def to_nines(seq):
    return str(int(pow(10, len(seq))-1))

def main():
    num_of_inputs = int(input())
    for ith_input in range(1, num_of_inputs+1):
        sequence = str(int(input().strip()))
        print("Case #{}: {}".format(ith_input, last_tidy(sequence)))

if __name__ == "__main__":
    main()
