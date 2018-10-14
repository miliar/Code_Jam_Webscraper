#Coded by Jeff Garcia, (one day I shall triumph, but not today)

def main():
    output_file = open("/home/koofu/PycharmProjects/CodeJam/output.out", 'w')

    with open("/home/koofu/PycharmProjects/CodeJam/C-small-1-attempt1.in", 'r') as f:
        test_cases = f.readline().strip()
        for counter, rawline in enumerate(f):
            if counter+1 > int(test_cases):
                break
            line = rawline.strip()
            output_file.write("Case #{0}: {1}".format(counter+1, solve(line)+'\n'))


def solve(stripped_line):
    split_line = stripped_line.split()
    queue = list()
    queue.append(int(split_line[0]))
    for i in range(int(split_line[1])):
        queue.sort(reverse=True)
        value = queue.pop(0) -1
        holder = ((value)//2)+((value) % 2)
        if holder == 0:
            return "0 0"
        queue.append(holder)
        queue.append((value)//2)
    return "{0} {1}".format(queue[-2], queue[-1])


if __name__ == "__main__":
    main()
