import sys
from copy import deepcopy


DEBUG = False


def printstrings(strings):
    print '------'
    for s in strings:
        print ''.join(s)


def chars_at(i, strings):
    chars = set()
    for s in strings:
        if len(s) > i:
            chars.add(s[i])
        else:
            chars.add(None)
    return chars


def solve(strings):
    i = 0
    total_cost = 0
    if DEBUG:
        printstrings(strings)
    while i < max(len(s) for s in strings):
        #Chars at i-1 are all identical
        chars = chars_at(i, strings)
        if DEBUG:
            print "chars:", chars
        if len(chars) != 1:
            # some chars differ
            # Try to duplicate previous char
            adding_strings = deepcopy(strings)
            removing_strings = deepcopy(strings)
            adding_cost = None
            removing_cost = None
            if i != 0 and len(chars) < len(strings):
                # Only some characters differ
                # We need len(chars) actions to resolve by repeating
                adding_cost = 0
                for s_index in range(len(adding_strings)):
                    s = adding_strings[s_index]
                    if i >= len(s) or s[i] != s[i - 1]:
                        adding_strings[s_index] = s[:i] + [s[i - 1]] + s[i:]
                        adding_cost += 1
                if DEBUG:
                    print 'adding', adding_cost
            if i != 0:
                cost = 0
                for s_index in range(len(removing_strings)):
                    s = removing_strings[s_index]
                    for j in range(i, len(s) + 1):
                        if j >= len(s) or s[i - 1] != s[j]:
                            break
                    if j >= len(s) or (j > i and s[j] in chars):
                        removing_strings[s_index] = s[:i] + s[j:]
                        cost += j - i
                if DEBUG:
                    print 'removing', cost
                if len(chars_at(i, removing_strings)) == 1:
                    removing_cost = cost
            if adding_cost or removing_cost:
                if adding_cost:
                    if removing_cost and removing_cost < adding_cost:
                        strings = removing_strings
                        total_cost += removing_cost
                    else:
                        strings = adding_strings
                        total_cost += adding_cost
                else:
                    strings = removing_strings
                    total_cost += removing_cost
            else:
                # Couldn't add or remove strings to match strings
                return "Fegla Won"
        i += 1

        if DEBUG:
            printstrings(strings)
    return total_cost


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    i = 1
    case = 1
    while i < len(lines):
        n = int(lines[i].strip())
        strings = map(lambda l: list(l.strip()), lines[i + 1:i + n + 1])
        sol = solve(strings)
        print "Case #%d: %s" % (case, sol)
        case += 1
        i += n + 1
        #sys.exit(0)
