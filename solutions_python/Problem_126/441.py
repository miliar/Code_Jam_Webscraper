vowels = ['a', 'e', 'i', 'o', 'u']

def count_n(line):
    max_n = 0
    current_n = 0
    for c in line:
        if c in vowels:
            max_n = max(max_n, current_n)
            current_n = 0
        else:
            current_n += 1
    max_n = max(max_n, current_n)
    return max_n

def main():
    T = int(raw_input())
    for ti in range(T):
        inputs = raw_input().split()
        name = inputs[0]
        n = int(inputs[1])
        ans = 0
        for i in range(len(name)):
            for j in range(i+1, len(name)+1):
                if count_n(name[i:j]) >= n:
                    ans += 1
        print "Case #{0}: {1}".format(ti+1, ans)
    pass

if __name__ == "__main__":
    main()
