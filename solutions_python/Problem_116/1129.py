import sys

def fopen():
    return open(sys.argv[1], 'r')

def readline(input):
    return input.readline().strip("\n").strip("\r")


def total_cases(input):
    return int(readline(input))


def process(handler):
    input = fopen()
    for case_num in range(total_cases(input)):
        handler(case_num + 1, input)

    input.close()
