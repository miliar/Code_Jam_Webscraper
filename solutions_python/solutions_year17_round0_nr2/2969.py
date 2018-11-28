INPUT_FILE = 'B-large.in'
OUTPUT_FILE = 'B-large.out'

def read_file():
    with open(INPUT_FILE) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        f.close()
    return content


def is_tidy(n_string):
    aux = 0
    for i in range(len(n_string)):
        if (n_string[i] >= aux):
            aux = n_string[i]
        else:
            return False
    return True


def find_tidy_number(n_string):
    for j in range(len(n_string), 0, -1):
        spliced_n = n_string[j - 1:]
        if(is_tidy(spliced_n)):
            pass
        else:
            spliced_n = str(int(spliced_n[0]) - 1) + '9' * (len(spliced_n) - 1)
            n_string = n_string[:j - 1] + spliced_n
    return str(int(n_string))


def main(file_in):
    with open(OUTPUT_FILE, 'w') as f:
        size_file = int(file_in[0])
        for i in range(1, size_file + 1):
            tidy_number = 0
            input_n = file_in[i]
            result = find_tidy_number(input_n)
            f.write('Case #{0}: {1} \n'.format(i, result))

main(read_file())
