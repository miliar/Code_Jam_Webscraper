INPUT_FILE = 'A-large.in'
OUTPUT_FILE = 'A-large.out'


def read_file():
    with open(INPUT_FILE) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        content = [x.split() for x in content]
        return content

def find_min_flips(pancakes, k):
    count = 0
    for j in range(len(pancakes) - k + 1):
        flipable = list(pancakes[j:(j + k)])
        if flipable[0] == '-':
            for l in range(len(flipable)):
                if flipable[l] == '-':
                    flipable[l] = '+'
                else:
                    flipable[l] = '-'
            pancakes =  pancakes[0:j] + "".join(flipable) + pancakes[j + k:]
            count += 1
    if pancakes != ('+' * len(pancakes)):
        count = 'IMPOSSIBLE'
    return count

def main():
    with open(OUTPUT_FILE, 'w') as f:
        file_in = read_file()
        size_file = int(file_in[0][0])
        for i in range(1, size_file + 1):
            pancakes = file_in[i][0]
            k = int(file_in[i][1])
            count = find_min_flips(pancakes,k)
            f.write('Case #{0}: {1} \n'.format(i, count))



main()
