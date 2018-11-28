#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <limits>
#include <algorithm>
#include <exception>
using namespace std;

using num_t             = int64_t;
using range_t           = pair<num_t, num_t>;
constexpr num_t INF_FAR = numeric_limits<num_t>::max();

range_t smartMethod(num_t n, num_t k) {
    // sum of all the splits
    num_t splitRound = 0;
    num_t splitSum   = n;

    num_t lastL = 0;
    num_t lastR = 0;

    while (k > 0) {
        // how many times this round will split
        num_t splitNum = pow(2, splitRound);
        // each split we decrease the sum by 1
        splitSum -= splitNum;

        // { cout << "split " << splitNum << " times to sum to " << splitSum << endl; }

        // sum of the lastL and lastR
        num_t individualSplitSum = splitSum / splitNum;     // rounded down
        lastL                    = individualSplitSum / 2;  // rounded down
        // even means lastL == lastR, else lastR > lastL
        if (individualSplitSum % 2 == 0) {
            lastR = lastL;
        } else {
            lastR = lastL + 1;
        }
        // sum does not divide evenly into the splits, we'll put it in the first split
        num_t leftOver = splitSum % splitNum;

        // {
        //     cout << "L:" << lastL << " R:" << lastR << endl;
        //     cout << "leftover: " << leftOver << endl;
        // }

        // consider if the spltting ends here
        if (k < splitNum) {
            // special treatment since we still have leftovers
            if (k <= leftOver) {
                if (lastL < lastR) {
                    lastL += 1;
                } else {
                    lastR += 1;
                }
            }
            return {max(lastL, lastR), min(lastL, lastR)};
        } else {
            // "perform" the splits and move onto next round
            k -= splitNum;
            splitRound += 1;
        }
    }

    return {max(lastL, lastR), min(lastL, lastR)};
}

int main() {
    int T;
    cin >> T;

    for (int c = 1; c <= T; ++c) {
        // integer
        num_t n, k;
        cin >> n >> k;

        auto maxMin = smartMethod(n, k);

        cout << "Case #" << c << ": " << maxMin.first << " " << maxMin.second << endl;
    }
}