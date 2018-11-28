#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <cassert>
using namespace std;


long long findPlacement(long long numStalls, long long numUsers) {
    assert(numUsers <= numStalls);
    map<long long, long long> counts;
    counts[numStalls] = 1;
    while (true) {
        auto it = counts.end();
        --it;
        auto e = *it;
        counts.erase(it);
        if (e.second < numUsers) {
            counts[(e.first - 1) / 2] += e.second;
            counts[e.first / 2] += e.second;
            numUsers -= e.second;
        } else {
            return e.first;
        }
    }
}


int getPlacement(const vector<bool>& state) {
    int l = 0;
    while (l < state.size() && state[l]) ++l;
    int bestL, bestR;
    bestL = bestR = -1;
    while (l < state.size()) {
        int r = l;
        while (!state[r]) ++r;
        if (bestL == -1 || r - l > bestR - bestL) {
            bestL = l;
            bestR = r;
        }
        l = r;
        while (l < state.size() && state[l]) ++l;
    }
    assert(bestL != -1);
    return bestL + (bestR - bestL - 1) / 2;
}


int findPlacementNaive(int numStalls, int numUsers) {
    vector<bool> state(numStalls + 2);
    state[0] = state.back() = true;
    while (numUsers > 1) {
        int placement = getPlacement(state);
        state[placement] = true;
        --numUsers;
    }
    int placement = getPlacement(state);
    int l = placement, r = placement;
    while (!state[l - 1]) --l;
    while (!state[r]) ++r;
    return r - l;
}


void stressTest() {
    for (int n = 1; n <= 100; ++n) {
        for (int k = 1; k <= n; ++k) {
            long long naiveAns = findPlacementNaive(n, k);
            long long smartAns = findPlacement(n, k);
            if (naiveAns != smartAns) {
                cerr << "Answers don't match for n = " << n << " k = " << k << " naive = " << naiveAns << " smart = " <<
                smartAns << endl;
                return;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int numTests;
    cin >> numTests;
    for (int testId = 0; testId < numTests; ++testId) {
        long long numStalls, numUsers;
        cin >> numStalls >> numUsers;
        long long placementEmptyStallsCount = findPlacement(numStalls, numUsers);
        cout << "Case #" << testId + 1 << ": "
             << placementEmptyStallsCount / 2 << " "
             << (placementEmptyStallsCount - 1) / 2 << endl;
    }
    return 0;
}
