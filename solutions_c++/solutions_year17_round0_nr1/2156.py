#include <algorithm>
#include <bitset>
#include <complex>
#include <cstdio>
#include <cstdint>
#include <cassert>
#include <cmath>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

using int64 = int64_t;

constexpr int64 MOD = 1000000007;

string solve(string S, int K) {
    const int len = S.size();

    // flip left to right with the oversized flipper
    int num_flips = 0;
    for (int j = 0; j < len-K+1; ++j) {
        if (S[j] == '-') {
            ++num_flips;
            for (int l = j; l < j+K; ++l) {
                S[l] = (S[l] == '-') ? '+' : '-';
            }
        }
    }

    // check whether all pancakes are happy side up
    for (int j = 0; j < len; ++j) {
        if (S[j] == '-') {
            return "IMPOSSIBLE";
        }
    }
    
    stringstream ss;
    ss << num_flips;
    return ss.str();
}

int main() {
    int T; cin >> T;
    for (int j = 0; j < T; ++j) {
        string s; int k;
        cin >> s >> k;

        cout << "Case #" << (j+1) << ": " << solve(s, k) << endl;
    }
    return 0;
}
