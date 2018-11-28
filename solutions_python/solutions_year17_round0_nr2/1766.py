"""Tidy"""
import fileinput

def generate_tidy(number):
    """Generate the next lowest tidy"""
    length = len(number)
    for i in range(length - 1, 0, -1):
        if number[i] < number[i-1]:
            number[i:length] = [9]*(length-i)
            number[i-1] -= 1
    return int(''.join(str(x) for x in number))


def main():
    """Main Method"""
    handler = fileinput.input()
    number = int(handler.readline())
    for case in range(1, number+1):
        highest = handler.readline().strip()
        last_tidy = generate_tidy([int(x) for x in highest])

        print('Case #{case}: {last_tidy}'.format(case=case, last_tidy=last_tidy))

if __name__ == '__main__':
    main()
