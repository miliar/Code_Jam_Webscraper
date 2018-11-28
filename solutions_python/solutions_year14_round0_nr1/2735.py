import sys

def find_match(dataset):
    cases = []

    for i in range(1, dataset[0] + 1):
        count = 0

        af1 = dataset[i]['af']
        as1 = dataset[i]['as']

        ans = -1

        for j in dataset[i]['fa'][af1-1]:
            if j in dataset[i]['sa'][as1-1]:
                count = count + 1
                ans = j

        if count == 0:
            cases.append("Volunteer cheated!")
        elif count == 1:
            cases.append(str(ans))
        elif count > 1:
            cases.append("Bad magician!")

    return cases

def read_input(fname):
    f = open(fname, 'r')

    ncases = int(f.readline())

    dataset = []

    dataset.append(ncases)

    for i in range(ncases):
        data = {}
        data['af'] = int(f.readline())
        data['fa'] = []

        for i in range(4):
            row = []
            for n in f.readline().split():
                row.append(int(n))
            data['fa'].append(row)

        data['as'] = int(f.readline())
        data['sa'] = []

        for i in range(4):
            row = []
            for n in f.readline().split():
                row.append(int(n))
            data['sa'].append(row)

        dataset.append(data)

    return dataset

def write_output(cases):
    for i in range(len(cases)):
        print "Case #" + str(i+1) + ":", cases[i]


def main():
    if len(sys.argv) != 2:
        print "Please specify an input file."
        return

    dataset = read_input(sys.argv[1])

    cases = find_match(dataset)

    write_output(cases)
    
if __name__ == "__main__":
    main()
