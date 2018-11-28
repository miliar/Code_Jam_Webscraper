def get_phone_number(S):
    number_counts = [0] * 10
    for letter in S:
        if letter == 'U':
            number_counts[4] += 1
        elif letter == 'Z':
            number_counts[0] += 1
        elif letter == 'W':
            number_counts[2] += 1
        elif letter == 'X':
            number_counts[6] += 1
        elif letter == 'G':
            number_counts[8] += 1
        elif letter == 'F':
            number_counts[5] += 1
        elif letter == 'V':
            number_counts[7] += 1
        elif letter == 'R':
            number_counts[3] += 1
        elif letter == 'O':
            number_counts[1] += 1
        elif letter == 'N':
            number_counts[9] += 1

    number_counts[5] -= number_counts[4]
    number_counts[7] -= number_counts[5]
    number_counts[3] -= number_counts[0] + number_counts[4]
    number_counts[1] -= number_counts[0] + number_counts[2] + number_counts[4]
    number_counts[9] -= number_counts[1] + number_counts[7]
    number_counts[9] /= 2
    phone_number = ''
    for i in range(10):
        phone_number += str(i) * number_counts[i]
    return phone_number

def main():
    f_in = open('A-large.in.txt', 'r')
    f_out = open('A-large.out.txt', 'w')

    n_tests = int(f_in.readline())
    for i in range(n_tests):
        S = f_in.readline()
        f_out.write('Case #{}: {}\n'.format(i + 1, get_phone_number(S)))

    f_in.close()
    f_out.close()

if __name__ == "__main__":
    main()
