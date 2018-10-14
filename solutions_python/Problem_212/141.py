import argparse
from decimal import *

def distribute(ps, k):

    ps = sorted(ps)

    outcomes = {0: Decimal(1)}
    for p in ps:
        new_outcomes = {}

        for successes, prob in outcomes.iteritems():
            if successes in new_outcomes:
                new_outcomes[successes] += (1-p) * prob
            else:
                # print ps, p
                new_outcomes[successes] = (1 - p) * prob
            new_outcomes[successes+1] = p * prob

        outcomes = new_outcomes

    total_prob = Decimal(0)
    sum_probs = 0
    for successes, prob in outcomes.iteritems():
        if successes >= k:
            total_prob += prob
        sum_probs += prob

    return total_prob


def train(n, u, ps):
    ps = ps[:]

    # train everything to the max
    if u + sum(ps) >= n:
        return [Decimal(1)] * n

    num_to_raise = 1

    while u > 0.0000001:
        if num_to_raise == n:
            max_to_raise = 1.0
        else:
            max_to_raise = ps[num_to_raise] - ps[num_to_raise - 1]

        amt_to_add = min (u / num_to_raise, max_to_raise)
        for pi in range(0, num_to_raise):
            ps[pi] += amt_to_add
            u -= amt_to_add

        num_to_raise += 1

    return ps


def main(f_in, f_out):

    num_cases = int(f_in.readline().strip())
    for case in range(1, num_cases+1):


        n, p = [int(x) for x in f_in.readline().strip().split()]
        gs = [int(x) for x in f_in.readline().strip().split()]

        mod_gs = [g % p for g in gs]

        num_0s = mod_gs.count(0)
        num_1s = mod_gs.count(1)
        num_2s = mod_gs.count(2)
        num_3s = mod_gs.count(3)

        out = 0
        if p == 2:
            out += num_0s
            out += num_1s / 2
            if num_1s % 2 == 1:
                out += 1
        if p == 3:
            out += num_0s
            out += min(num_1s, num_2s)
            out += abs(num_1s - num_2s) / 3
            if abs(num_1s - num_2s) % 3 != 0:
                out += 1
        if p == 4:
            out += num_0s
            out += num_2s / 2
            out += min(num_1s, num_3s)
            if num_2s % 2 == 0:
                out += abs(num_1s - num_3s) / 4
                if abs(num_1s - num_3s) % 4 != 0:
                    out += 1
            if num_2s % 2 == 1:
                out += 1
                out += max(abs(num_1s - num_3s) - 2, 0) / 4
                if max(abs(num_1s - num_3s) - 2, 0) % 4 != 0:
                    out += 1

        f_out.write('Case #{}: {}\n'.format(case, out))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')

    opts = parser.parse_args()
    infile = opts.infile
    outfile = infile.split('.')[0]+'.out'
    print "Solving! in: {} -> out: {}".format(infile, outfile)

    with open(infile, 'r') as f_in:
        with open(outfile, 'w') as f_out:
            main(f_in, f_out)
