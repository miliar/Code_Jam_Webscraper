#!/usr/bin/python3

__author__ = 'Varun Barad'

def main():
    no_of_cases = int(input())

    for i in range(no_of_cases):
        line = input()
        s_max = int(line.split()[0])
        audience = []
        for c in line.split()[1]:
            audience.append(int(c))
        current = 0
        required = 0
        for j in range(len(audience)):
            if current >= j:
                current += audience[j]
            elif audience[j] > 0:
                required += j - current
                current += audience[j] + required

        answer = 'Case #{0}: {1}'.format((i + 1), required)
        print(answer)

if __name__ == '__main__':
    main()
