import argparse


def get_increasing_number(num):
    while not all_increasing(num):
        num = change_num(num)
    return num


def all_increasing(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True

def change_num(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            # 0 should never get here, so this should strip all 
            return (num[:i] + str(int(num[i])-1) + "9" * (len(num) - 1 - i)).lstrip("0")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="output_file", help="output file")
    args = parser.parse_args()

    with open(args.output_file) as f, open(args.output_file.replace("in.txt", "out.txt"), "w") as out:
        test_cases = int(f.readline().strip())
        for i, _ in enumerate(range(test_cases)):
            out.write("Case #{}: {}\n".format(i+1, get_increasing_number(f.readline().strip())))


if __name__ == "__main__":
    main()
