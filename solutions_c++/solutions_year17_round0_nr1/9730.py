// https://code.google.com/codejam/contest/3264486/dashboard#s=p0
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
#include <memory>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <bitset>
#include <set>

//#include "../../common/debug.h"

using namespace std;

using bs = bitset<10>;

bool solve_rec(bs& pns, int l, int k, unordered_map<bs,int>& solutions) {
    solutions[pns] = INT_MAX;
    //cout << " " << pns << endl;
    bool found = true;
    for (int i = 0; i < l; ++i) {
        if (!pns[i]) {
            found = false;
            break;
        }
    }
    if (found) {
        solutions[pns] = 0;
        return true;
    }
    int shortest = INT_MAX;
    for (int i = 0; i <= l-k; ++i) {
        for (int j = i; j < i+k; ++j) {
            pns.flip(j);
        }
        if (solutions.find(pns) == solutions.end()) {
            solve_rec(pns, l, k, solutions);
        }
        if (solutions[pns] < INT_MAX)
            shortest = min(solutions[pns] + 1, shortest);
        for (int j = i; j < i+k; ++j) {
            pns.flip(j);
        }
    }
    solutions[pns] = shortest;
    return shortest < INT_MAX;
}

int main() {
    int t; cin >> t;

    for (int i = 0; i < t; ++i) {
        string pns_str; cin >> pns_str; int k; cin >> k;

        cout << "Case #" << i+1 << ": ";

        bs pns;
        for (unsigned long j = 0; j < pns_str.length(); ++j) {
            pns[j] = pns_str[j] == '+';
        }

        unordered_map<bs,int> solutions;

        solve_rec(pns, pns_str.length(), k, solutions);
        if (solutions[pns] == INT_MAX)
            cout << "IMPOSSIBLE";
        else
            cout << solutions[pns];

        cout << endl;
    }

    return 0;
}
