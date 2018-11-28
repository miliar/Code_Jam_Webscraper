"""Pancakes"""
import fileinput

def main():
    """Main Method"""
    handler = fileinput.input()
    appearences = int(handler.readline())
    for case in range(1, appearences+1):
        flips = 0
        row, flipper = handler.readline().strip().split()
        row = list(row)
        flipper = int(flipper)
        try:
            for i, pancake in enumerate(row):
                if pancake == '-':
                    flips += 1
                    for j in range(i, i + flipper):
                        if row[j] == '-':
                            row[j] = '+'
                        else:
                            row[j] = '-'
            print(f'Case #{case}: {flips}')
        except IndexError:
            print(f'Case #{case}: IMPOSSIBLE')

if __name__ == '__main__':
    main()
