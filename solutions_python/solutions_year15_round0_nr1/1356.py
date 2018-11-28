def resolve(countString):
    assembly = [0] + [int(n) for n in countString]

    notEnough = True
    while notEnough:
        for i in range(len(assembly)):
            notEnough = False
            shyest = assembly[:i]
            if sum(shyest) < i:
                assembly[0] += 1
                notEnough = True
                break
    return assembly[0]-1

if __name__ == '__main__':
    import csv, sys
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        # skip header
        next(reader, None)
        idx = 0
        for line in reader:
            idx += 1
            solution = resolve(line[1])
            print('Case #'+str(idx)+': ' + str(solution))
