import math

def handle_input(line):
    line = line.split(" ")
    lower_bound = int(math.ceil(math.sqrt(int(line[0]))))
    upper_bound = int(math.floor(math.sqrt(int(line[1]))))
    count = 0

    for i in range(lower_bound, upper_bound + 1):
        if is_palindrome(i) and is_palindrome(i ** 2):
            count += 1
        i += 1

    print_case(str(count))

def is_palindrome(i):
    return str(i) == str(i)[::-1]

case = 0
def print_case(out):
    global case
    case += 1
    print "Case #%i: %s" % (case, out)


with open("in.txt") as fin:
    lines = fin.read().split("\n")

# Remove newlines
while "" in lines:
    lines.remove("")

print "%s cases" % lines[0];
cases = int(lines[0])
lines = lines[1:]


for i in range(0, cases):
    handle_input(lines[i])