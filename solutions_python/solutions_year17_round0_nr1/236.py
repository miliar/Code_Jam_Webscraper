def main():
    with open('/Users/tengg/Downloads/A-large.in') as f:
        t = int(f.readline())
        for i in range(1, t+1):
            cakes, k = f.readline().split(' ')
            print(f"Case #{i}: " + minFlips(list(cakes), int(k)))

def minFlips(cakes, k):
    i = c = 0
    while i < len(cakes):
        if cakes[i] == '+':
            i+=1
            continue
        elif i + k > len(cakes):
            return "IMPOSSIBLE"
        c += 1
        for j in range(k):
            if cakes[i+j] == '-':
                cakes[i+j] = '+'
            else:
                cakes[i+j] = '-'
        i+=1
    return str(c)

if __name__ == '__main__':
    main()