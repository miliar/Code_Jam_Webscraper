import sys
import time


if __name__ == "__main__":

    t1 = time.clock()

    f = open(sys.argv[1])
    testcount = int(f.readline())

    for testindex in range(0, testcount):

        line = f.readline()
        num_teams = int(line)

        resmatrix = []
        for teamindex in range(0, num_teams):

            line = f.readline()
            vals = line.strip()
            resmatrix.append(list(vals))

        """
        for i in range(0, num_teams):
            for j in range(0, num_teams):
                sys.stderr.write(resmatrix[i][j])
            sys.stderr.write('\n')
        """

        # WPS
        points = [0] * num_teams
        matchcounts = [0] * num_teams
        wps = [0.0] * num_teams
        for i in range(0, num_teams):
            for res in resmatrix[i]:
                if res == '.':
                    continue
                points[i] += int(res)
                matchcounts[i] += 1
            wps[i] = float(points[i]) / float(matchcounts[i])

        # OWPS
        owps = [0.0] * num_teams
        for i in range(0, num_teams):
            opponent_average_wp = 0.0
            for wpi in range(0, num_teams):
                if resmatrix[i][wpi] == '.':
                    continue
                numerator = float(points[wpi]) - float(resmatrix[wpi][i])
                denominator = matchcounts[wpi] - 1
                opponent_average_wp += float(numerator) / float(denominator)
            owps[i] = opponent_average_wp / matchcounts[i]

        # OOWPS
        oowps = [0.0] * num_teams
        for i in range(0, num_teams):
            opponent_average_owp = 0.0
            for owpi in range(0, num_teams):
                if resmatrix[i][owpi] == '.':
                    continue
                opponent_average_owp += owps[owpi]
            oowps[i] = opponent_average_owp / matchcounts[i]

        rpis = [0.0] * num_teams
        for i in range(0, num_teams):
            rpis[i] = 0.25 * wps[i] + 0.50 * owps[i] + 0.25 * oowps[i]

        print "Case #%i:" % (testindex+1)
        for i in range(0, num_teams):
            print rpis[i]


    t2 = time.clock()
    sys.stderr.write("runtime: %s\n" % repr(t2-t1))
