# pylint: disable=missing-docstring
import sys


def problem(numSeats, numCustomers, tickets):
    customers = [[] for n in range(numCustomers)]
    positions = [[] for n in range(numSeats)]
    for position, customer in tickets:
        customers[customer].append(position)
        positions[position].append(customer)
    customers = [sorted(x) for x in customers]
    customerLens = [len(x) for x in customers]
    tickets.sort(key=lambda x: x[0])
    needed = 0
    for i in range(1, numSeats + 1):
        needed = max(needed, sum([len(x) for x in positions[:i]]) // i)
    ridesNeeded = max(needed, max(customerLens))
    promotionsNeeded = sum([max(0, len(x) - ridesNeeded) for x in positions])
    return f'{ridesNeeded} {promotionsNeeded}'






def nextline(input_file):
    data = ""
    while not data:
        data = input_file.readline()
    return data[:-1]

def intsplit(s):
    return [int(x) for x in s.split(" ")]


def main():
    result = ""
    with sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r') as infile:
        number = int(nextline(infile))
        for run in range(number):
            case = nextline(infile)
            numSeats, numCustomers, numTickets = intsplit(case)
            tickets = []
            for n in range(numTickets):
                position, customer = intsplit(nextline(infile))
                tickets.append((position - 1, customer - 1))
            result += 'Case #{}: {}\n'.format(1 + run, problem(numSeats, numCustomers, tickets))

    if len(sys.argv) == 1:
        print(result, end='')
    else:
        with open(sys.argv[1].replace('in', 'sol'), 'w') as result_file:
            result_file.write(result)

if __name__ == '__main__':
    main()
