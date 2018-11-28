#include <stdio.h>
#include <stdlib.h>

#include <vector>
#include <limits>

using namespace std;

vector<uint64_t> breaks;

pair<uint64_t, uint64_t> soln(uint64_t cells)
{
    if (cells % 2) {
        return make_pair((cells - 1) / 2, (cells - 1) / 2);
    } else {
        return make_pair(cells / 2, (cells - 1) / 2);
    }
}

pair<uint64_t, uint64_t> solve(uint64_t stalls, uint64_t people)
{
    --people;

    uint64_t split = stalls;
    uint64_t placed = 0;
    for (int i = 1; i < breaks.size(); ++i) {
        if (people < breaks[i]) {
            placed = breaks[i - 1];
            break;
        }
        --split;
        split /= 2;
    }

    // Now, we have some ranges with split stalls, and some ranges with
    // (split + 1) stalls.
    // We have a total of placed + 1 ranges.
    uint64_t longerRangeCount = stalls - placed - split * (placed + 1);
    //uint64_t shorterRangerCount = placed + 1 - longerRangeCount;

    if (longerRangeCount > people - placed) {
        // last person is going into a longer stall.
        return soln(split + 1);
    } else {
        return soln(split);
    }
}

int main(void)
{
    breaks.push_back(0);
    while (breaks.back() < numeric_limits<uint64_t>::max() / 2) {
        breaks.push_back((breaks.back() + 1) * 2 - 1);
    }

    /*
    for (uint64_t val : breaks) {
        printf("%llu\n", val);
    }
    */

    int nC;
    scanf("%d", &nC);
    for (int cC = 0; cC < nC; ++cC) {
        uint64_t N, K;
        scanf("%llu%llu", &N, &K);

        pair<uint64_t, uint64_t> ret = solve(N, K);
        printf("Case #%d: %llu %llu\n", cC + 1, ret.first, ret.second);
    }
    return 0;
}