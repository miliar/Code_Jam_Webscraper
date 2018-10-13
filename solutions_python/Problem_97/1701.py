def find_recycles(start, end):
    count = 0
    
    for i in range(start, end+1):
        for j in range(i+1, end+1):
            candidate = str(i) + str(i)
            candidate = candidate[1:-1]
            if str(j) in candidate:
                count += 1

    return count

def main():
    f = open('input.txt')
    num_cases = int(f.readline())

    for i in range(1, num_cases + 1):
        case = f.readline().strip('\n')
        data = case.split()
        out = find_recycles(int(data[0]), int(data[1]))
        print "Case #" + str(i) + ": " + str(out)

if __name__ == '__main__':
    main()
