
def all_positive(pancakes):
    for pancake in pancakes:
        if not pancake:
            return False
    return True

def main(line):
    pancakes, flipper_str = line.split()
    pancakes = [pancake == '+' for pancake in pancakes]
    flipper = int(flipper_str)
    num_pancakes = len(pancakes)
    count = 0
    for idx, pancake in enumerate(pancakes):
        if not pancake:
            count += 1
            if idx + flipper <= num_pancakes:
                for i in range(flipper):
                    pancakes[idx + i] = not pancakes[idx + i]
            else:
                return "IMPOSSIBLE"
    if all_positive(pancakes):
        return count
    return "IMPOSSIBLE"

if __name__ == '__main__':
    with open('A-small.out', 'w') as outfile:
        with open('A-small.in', 'r') as file:
            for idx, line in enumerate(file.readlines()):
                if idx == 0:
                    continue
                else:
                    outfile.write("Case #{}: {}\n".format(idx, main(line)))


            