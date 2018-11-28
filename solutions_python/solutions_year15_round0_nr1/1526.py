import sys


def solve(instream):
    line = instream.readline()
    people = [int(x) for x in line.strip().split(" ")[1]]
    invitations = 0
    num_people = 0
    for i in range(len(people)):
        if num_people < i:
            invitations += i - num_people
            num_people += i - num_people

        num_people += people[i]

    return invitations


def run(input=sys.stdin):
    cases = int(input.readline().strip())
    for i in range(cases):
        print("Case #{}: {}".format(i + 1, solve(input)))

if __name__ == "__main__":
    run()
