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

string solve(const int64 N) {
    stringstream ss; ss << N;
    string S; ss >> S; // S is a string representation of N

    string ans;
    char prev_dig = '0';
    for (int j = 0; j < S.size(); ++j) {
        if (prev_dig > S[j]) {
            // the rest of digits are nine
            for (int k = j; k < S.size(); ++k) {
                ans.push_back('9');
            }

            for (int k = j-1; k > 0; --k) {
                if (ans[k] >= '1' && ans[k]-1 >= ans[k-1]) {
                    ans[k] = ans[k]-1;
                    return ans;
                }
                ans[k] = '9';
            }

            if (ans[0] <= '1') {
                return ans.substr(1);
            }

            ans[0] = ans[0]-1;
            return ans;
        }

        ans.push_back(S[j]);
        prev_dig = S[j];
    }

    return ans;
}

int main() {
    int T; cin >> T;
    for (int j = 0; j < T; ++j) {
        int64 N; cin >> N;
        cout << "Case #" << (j+1) << ": " << solve(N) << endl;
    }
    return 0;
}
