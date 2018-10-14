
def invertFace(lst, index, flipper_size):
    for i in xrange(index, index + flipper_size):
        lst[i] = '+' if lst[i] == '-' else '-'


def runCount(string):
    tokens = string.split()
    lst = list(tokens[0])
    string_len = len(lst)
    flipper_size = int(tokens[1])
    count = 0

    for k in xrange(string_len - flipper_size + 1):
        if (lst[k] == '-'):
            count += 1
            invertFace(lst, k, flipper_size)
    
    if "-" in lst[k:]:
        return "IMPOSSIBLE"
    else:
        return count


def main():
    t = int(raw_input())
    for num in xrange(t):
        str = raw_input()
        print ("Case #{}: {}").format(num+1, runCount(str))

if __name__ == '__main__':
    main()
