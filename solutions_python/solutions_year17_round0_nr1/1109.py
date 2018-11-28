def flip_master(sequence, size):
    count = 0
    while len(sequence) >= size:
        if sequence[0] == "-":
            count += 1
            sequence = flip(sequence[:size]) + sequence[size:]
        sequence = sequence[1:]
    for char in sequence:
        if char == "-":
            return "IMPOSSIBLE"
    return count

def flip(sequence):
    new_sequence = ""
    for char in sequence:
        if char == "+":
            new_sequence += "-"
        else:
            new_sequence += "+"
    return new_sequence

def main():
    num_of_inputs = int(input())
    for ith_input in range(1, num_of_inputs+1):
        sequence, flip_size = input().strip().split()
        print("Case #{}: {}".format(ith_input, flip_master(sequence, int(flip_size))))

if __name__ == "__main__":
    main()
