import sys


def solution(line):
    count = 0
    invited = 0
    for i, num in enumerate(line):
        if count < i:
            count += 1
            invited += 1
        count += int(num)
    return invited


def main():
    sys.stdin.readline()
    sys.stdout.writelines('Case #%d: %d\n' % (i + 1, solution(line.split()[1]))
                          for i, line in enumerate(sys.stdin))


if __name__ == '__main__':
    main()
