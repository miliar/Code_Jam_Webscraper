import itertools
import random
import sys


if __name__ == '__main__':
    # Look at the solutions for n=3 to see if we can learn anything from it
    def compete(n, tl):
        """Return a list of the teams ordered by rank, assuming they competed based on the given tournament list."""
        number_of_teams = 1
        for i in range(n):
            number_of_teams *= 2
        # Simulate each round. Each round we partition the existing equivalence sets in half; after the last round each equivalence set will have one element representing the team at that rank.
        equiv = [tl]
        partition_size = number_of_teams
        for i in range(n):
            new_equiv = []
            for k in range(len(equiv)):
                winners = []
                losers = []
                for j in range(partition_size / 2):
                    if equiv[k][2 * j] < equiv[k][2 * j + 1]:
                        winners.append(equiv[k][2 * j])
                        losers.append(equiv[k][2 * j + 1])
                    else:
                        losers.append(equiv[k][2 * j])
                        winners.append(equiv[k][2 * j + 1])
                new_equiv.append(winners)
                new_equiv.append(losers)
            equiv = new_equiv
            partition_size /= 2
        return [x[0] for x in equiv]    

    def competition_statistics(n):
        number_of_teams = 1
        for i in range(n):
            number_of_teams *= 2
        team_numbers = list(range(number_of_teams))
        #tournament_lists = [list(x) for x in itertools.permutations(team_numbers)]
        tournament_lists = []
        for i in range(10000000):
            random.shuffle(team_numbers)
            tournament_lists.append([x for  x in team_numbers])
        team_numbers = sorted(team_numbers)
        best = [False] * number_of_teams
        worst = [False] * number_of_teams
        for tournament_list in tournament_lists:
            result = compete(n, tournament_list)
            for r, x in enumerate(result):
                if not best[x]:
                    best[x] = r
                    worst[x] = r
                best[x] = min(best[x], r)
                worst[x] = max(worst[x], r)
        for k in range(number_of_teams):
            print("For %d, best possible is %d, worst possible is %d" % (k, best[k], worst[k])) 

    # competition_statistics(4)

    def rankings(n):
        """Returns the [best_rank, worst_rank] for each team number. 0-indexed."""
        best = []
        worst = []
        def f(i):
            if i == n:
                return 1
            else:
                return 2 ** i
        def g(i):
            if i == 0:
                return 1
            else:
                return 2 ** (n - i)
        for i in range(n + 1):
            worst.extend([2 ** n - 2 ** (n - i)] * f(i))
            best.extend([2 ** i - 1] * g(i))
        return zip(best, worst)

    T = int(sys.stdin.readline())
    for z in range(1, T + 1):
        n, p = [int(x) for x in sys.stdin.readline().split()]
        rs = rankings(n)
        gauranteed = 0
        could = 0
        for i in range(len(rs)):
            best, worst = rs[i]
            if worst < p:
                gauranteed = i
            if best < p:
                could = i
        print("Case #%d: %d %d" % (z, gauranteed, could))
