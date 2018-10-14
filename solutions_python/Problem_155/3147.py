import sys

def get_input():
    T = int(raw_input())
    list = []
    for i in range(T):
        line = raw_input().split()
        list.append(line)
    return list

def print_results(T, output):
    for i in range(T):
        print "Case #%d: %d" %(i+1, output[i])

def invitations(s_max, string):
    s_max = int(s_max)
    string = [int(string[i]) for i in range(s_max+1)]
    invites = 0
    if s_max == 0:
        invites = 0
    else:
        for i in range(s_max+1):
            standing = sum(string[:i]) + invites
            diff = abs(standing - i)
            if standing < i and int(string[i])>0:
                invites = invites + diff
    return invites

def main():
    list = get_input()
    T = len(list)
    results = []
    for i in range(T):
        results.append(invitations(list[i][0], list[i][1]))
    print_results(T, results)

if __name__ == "__main__":
    main()
