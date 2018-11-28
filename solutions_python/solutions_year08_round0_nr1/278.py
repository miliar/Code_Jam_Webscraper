#!/usr/bin/python

from optparse import OptionParser

def main():
    USAGE = "usage: %prog [option]"
    parser = OptionParser(usage=USAGE)
    (options, args) = parser.parse_args()

    file_in = args[0]
    fi = file(file_in, 'r')
    N = int(fi.readline().rstrip('\n'))

    Infinite = 1e100000
    solution = [Infinite]*N
    for n in range(0, N):
        #Parse Input for particular testcase
        S = int(fi.readline().rstrip('\n'))
        listS = []
        for s in range(0, S):
            listS.append(fi.readline().rstrip('\n'))

        Q = int(fi.readline().rstrip('\n'))
        listQ = []
        for q in range(0, Q):
            listQ.append(fi.readline().rstrip('\n'))

        #
        #Find Solution
        #
        last_row = [0]*S    #Initial
        current_row = [0]*S

        # Iterate from largest q
        for iq in range(0, Q):
            q = Q-1-iq

            #Fill up current_row
            for s in range(0, S):
                min = Infinite
                cost4NotSwitch = 0
                if listQ[q] == listS[s]:
                    cost4NotSwitch = Infinite
                for ls in range(0, S):
                    cost = None
                    if s == ls:
                        cost = last_row[ls] + cost4NotSwitch
                    else:
                        cost = last_row[ls] + 1
                    if cost < min:
                        min = cost
                current_row[s] = min

            for s in range(0, S):
                last_row[s] = current_row[s]

        # Fill out solution for testcast : n
        for s in range(0, S):
            if last_row[s] < solution[n]:
                solution[n] = last_row[s]

    fi.close()

    #write output
    file_out = file_in[:len(file_in)-3] + ".out"
    fo = file(file_out, 'w')
    for n in range(0, N):
        fo.write("Case #%d: %d\n" %(n+1, solution[n]))
    fo.close()

if __name__ == "__main__":
    main()
