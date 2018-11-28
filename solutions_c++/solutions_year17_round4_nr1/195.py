#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using namespace std;

int memo3[128][128];
int memo4[128][128][128];

tuple<int, int, int> combinations[] = {
// { 0, 0, 0 },
{ 0, 1, 2 },
{ 0, 2, 0 },
// { 0, 3, 2 },
{ 1, 0, 1 },
// { 1, 1, 3 },
// { 1, 2, 1 },
// { 1, 3, 3 },
// { 2, 0, 2 },
{ 2, 1, 0 },
// { 2, 2, 2 },
// { 2, 3, 0 },
// { 3, 0, 3 },
// { 3, 1, 1 },
// { 3, 2, 3 },
// { 3, 3, 1 },
};

inline void try_improve(int& ans, int candidate) {
    if (candidate > ans) ans = candidate;
}

int solve3(int c1, int c2) {
    if (memo3[c1][c2] == -1) {
        int& ans = memo3[c1][c2] = 1;  // At least one group will benefit.
        if (c1 > 0 && c2 > 0) {
            try_improve(ans, 1 + solve3(c1 - 1, c2 - 1));
        }
        if (c1 >= 3) {
            try_improve(ans, 1 + solve3(c1 - 3, c2));
        }
        if (c2 >= 3) {
            try_improve(ans, 1 + solve3(c1, c2 - 3));
        }
    }
    return memo3[c1][c2];
}

int solve4(int c1, int c2, int c3) {
    if (memo4[c1][c2][c3] == -1) {
        int &ans = memo4[c1][c2][c3] = 1; // at least one group can benefit.
        // Try to combine 4 of them.
        if (c1 >= 4) try_improve(ans, 1 + solve4(c1 - 4, c2, c3));
        // if (c2 >= 4) try_improve(ans, 1 + solve4(c1, c2 - 4, c3));
        if (c3 >= 4) try_improve(ans, 1 + solve4(c1, c2, c3 - 4));
        if (c2 >= 1 && c3 >= 2) try_improve(ans, 1 + solve4(c1 - 0, c2 - 1, c3 - 2));
        if (c2 >= 2) try_improve(ans, 1 + solve4(c1, c2 - 2, c3));
        if (c1 >= 1 && c3 >= 1) try_improve(ans, 1 + solve4(c1 - 1, c2 - 0, c3 - 1));
        if (c1 >= 2 && c2 >= 1) try_improve(ans, 1 + solve4(c1 - 2, c2 - 1, c3 - 0));
    }
    return memo4[c1][c2][c3];
}

int main() {
    memset(memo3, 0xff, sizeof(memo3));
    memset(memo4, 0xff, sizeof(memo4));
    memo3[0][0] = 0;
    memo4[0][0][0] = 0;
    int num_cases;
    cin >> num_cases;
    for (int case_index = 1; case_index <= num_cases; ++case_index) {
        int P, N;
        cin >> N >> P;
        vector<int> mod_counts(P, 0);
        for (int i = 0; i < N; ++i) {
            int x;
            cin >> x;
            ++mod_counts[x % P];
        }
        // All zero base are as is.
        int ans = mod_counts[0];
        mod_counts.erase(mod_counts.begin());
        // Now handle the rest.
        if (P == 2) {
            ans += (mod_counts[0] + 1) / 2;
        } else if (P == 3) {
            ans += solve3(mod_counts[0], mod_counts[1]);
        } else if (P == 4) {
            ans += solve4(mod_counts[0], mod_counts[1], mod_counts[2]);
        }
        cout << "Case #" << case_index << ": " << ans << endl;
    }
    return 0;
}
