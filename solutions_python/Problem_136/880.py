#! /usr/bin/pypy

def solve(C,F,X):
    number_farms = 0

    growth_phase_time = 0
    constant_phase_time = X / 2.0

    best_duration_to_date = growth_phase_time + constant_phase_time

    while True:
        number_farms += 1

        time_to_next_farm = C / ((number_farms-1)*F + 2.0)
        growth_phase_time += time_to_next_farm

        constant_phase_time = X / (number_farms*F + 2.0)

        new_time = growth_phase_time + constant_phase_time

        if new_time > best_duration_to_date: #it goes up again
            break
        best_duration_to_date = new_time #else, we take that new time

    return "%0.7f" % best_duration_to_date

def processFile(filename):
    f = open(filename, "r")
    resultFile = open("result.txt","w")

    T = int(f.readline()) #number of cases in the first line
    print "Solving %s cases:"%(T,)

    #read the other lines
    solutions = []
    for i,line in enumerate(f.readlines()):
        s =  map(float,line.split(" ")) #split one line, convert to int
        C = s[0]
        F = s[1]
        X = s[2]

        a = "Case #%s: %s"%(i+1,solve(C,F,X)) #solution line
        solutions.append(a)
        print a

    resultFile.write("\n".join(map(str,solutions)))

    resultFile.close()
    f.close()

if __name__ == "__main__":
    # something which needs to be precomputed goes here

    while True:
        print "Input filename to solve:"
        fileNameToSolve = raw_input()
        processFile(fileNameToSolve)

        print "Results have been written to result.txt"
