from math import ceil

class repartition:
    def __init__(self, cost):
        self.first = True
        self.result = [1]*cost

    def __iter__(self):
        return self

    def __next__(self):
        if self.first:
            self.first = False
            return self.result

        if len(self.result) == 1:
            raise StopIteration

        if self.result[-1] == 1:
            self.result.pop(-1)
            for i in range(len(self.result)):
                if i == len(self.result) -1:
                    self.result[0] += 1
                    return self.result
                elif self.result[i] > self.result[i+1]:
                    self.result[i+1] += 1
                    return self.result
        else:
            self.result[-1] -= 1
            for i in range(len(self.result)):
                if i == len(self.result) - 2:
                    self.result[0] += 1
                    return self.result
                elif self.result[i] > self.result[i+1]:
                    self.result[i+1] += 1
                    return self.result


def share(number_of_transaction, pancakes):
    result = []
    for combination in repartition(number_of_transaction):
        new_repartition = []
        for i in range(len(pancakes)):
            if i > len(combination) - 1:
                new_repartition.append(pancakes[i])
            else:
                new_repartition.append(ceil(pancakes[i] / (combination[i] + 1)))
        result.append(max(new_repartition))
    return(min(result)+number_of_transaction)

def resolve(pancakes):
    pancakes = tuple(sorted([int(n) for n in pancakes], reverse=True))
    solution = pancakes[0]
    for number_of_transaction in range(1,pancakes[0]):
        solution = min(share(number_of_transaction, pancakes), solution)
    return solution

if __name__ == '__main__':
    import csv, sys
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        # skip header
        next(reader, None)
        next(reader, None)
        idx = 0
        for line in reader:
            idx += 1
            next(reader, None)
            solution = resolve(line)
            print('Case #'+str(idx)+': ' + str(solution))
