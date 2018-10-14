import argparse

def num_flips(pancakes, length):
    last = pancakes.rfind("-")
    result = 0
    while(last != -1):
        if last < length-1:
            return "IMPOSSIBLE"
        result += 1
        pancakes = make_new_pancake_stack(pancakes, last, length)
        last = pancakes.rfind("-")
    return result

def make_new_pancake_stack(pancakes, last, length):
    return pancakes[:last + 1 - length] + pancakes[last+1-length:last+1].translate(str.maketrans("+-", "-+"))

def format_output(results):
    return ["Case #{}: {}\n".format(i+1, r) for i, r in enumerate(results)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="input_file", help="input file")
    args = parser.parse_args()

    with open(args.input_file) as f, open(args.input_file.replace("in.txt", "out.txt"), "w") as out:
        num_examples = int(f.readline().strip())
        results = []
        for i in range(num_examples):
            pancakes, length = f.readline().strip().split()
            results.append(num_flips(pancakes, int(length)))
        out.write("".join(format_output(results)))

if __name__ == "__main__":
    main()
