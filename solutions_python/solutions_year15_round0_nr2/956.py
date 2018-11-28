def addSpecial(process):
    """apply special minute to process"""
    return (process[0] + 1, process[1])


def pancakeReduce(*processes):
    """Summarize an arbitrary number of processes to the best process that can be made from them

    Process can be described by how many special minutes and regular minutes are needed
    to solve.

    A process is represented by a tuple where the first element is the number of special
    minutes and the second element is the number of regular minutes.
    The sum of the two is the total time for the process to take place

    e.g. The process (1, 3) is a solution to solve a single plate with 4 pancakes
    """
    special_array, regular_array = zip(*processes)
    return (sum(special_array), max(regular_array))


def memo(func):
    cache = {}
    def _func(arg):
        if arg in cache:
            return cache[arg]
        result = func(arg)
        cache[arg] = result
        return result
    return _func


@memo
def possibleProcesses(plate_state):
    """Give a plate state (number of pancakes on singleplate)
    enumerate the possible processes that would solve the state

    Eliminates superfluous processes, i.e. repeated processes, and subprocesses like (1, 2) when (1, 3) exists
    """
    if plate_state == 0:
        return [(0, 0)]
    elif plate_state == 1:
        return [(0, 1)]
    else:
        child_states = [[state, plate_state - state] for state in range(1, (plate_state / 2) + 1)]
        processes = [(possibleProcesses(s[0]), possibleProcesses(s[1])) for s in child_states]
        result = [(0, plate_state)] + [
            addSpecial(pancakeReduce(p1, p2))
            for p1s, p2s in processes
            for p1 in p1s
            for p2 in p2s]
        result.sort()
        latest = -1
        real_result = []
        for r in result:
            if r[0] > latest and (not real_result or (r[1] < real_result[-1][1])):
                real_result.append(r)
                latest = r[0]
        return real_result


def pickNextIndiciesToIncrement(process_searchers, process_indicies, next_tries):
    max_eats = max(tries[1] for tries in next_tries)
    next_indicies = []
    for i, tries in enumerate(next_tries):
        if tries[1] == max_eats and process_indicies[i] + 1 < len(process_searchers[i]):
            next_indicies.append(i)
    return next_indicies


def howManyMinutes(plate_list):
    process_indicies = [0] * len(plate_list)
    process_searchers = map(possibleProcesses, plate_list)

    currentBest = None
    while True:
        next_tries = [process_list[process_indicies[i]]
            for i, process_list in enumerate(process_searchers)]
        check = sum(pancakeReduce(*next_tries))
        if not currentBest or check < currentBest:
            currentBest = check
        indicies = pickNextIndiciesToIncrement(process_searchers, process_indicies, next_tries)
        if not indicies:
            return currentBest
        for index in indicies:
            process_indicies[index] += 1


def test():
    assert pancakeReduce((1, 3), (2, 1)) == (3, 3)
    for i in range(100):
        possibleProcesses(i)

    assert howManyMinutes([4, 9]) == 6


if __name__ == "__main__":
    import sys
    import os
    filename = sys.argv[1]
    if filename == "test":
        test()
        print "Tests pass"
    else:
        with open(filename, "r") as inputfile:
            problems = inputfile.readlines()[2::2]
        test_cases = map(lambda row: map(int, row.split()), problems)

        solution_rows = []
        for i, plates in enumerate(test_cases):
            solution_rows.append("Case #%s: %s" % (i + 1, howManyMinutes(plates)))

        with open("solutions/" + os.path.basename(filename) + ".solution", "w+") as solutionfile:
            solutionfile.write("\n".join(solution_rows))
