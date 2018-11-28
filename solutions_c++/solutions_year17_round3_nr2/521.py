#include <iostream>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <iomanip>
#include <queue>
#include <utility>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<int, char> pci;

const int kN = 1000;
const int kD = 24 * 60;
const int kInf = 1e9;

int dp[kN][kN][3][3];
int used[2][kD];

int Dp(int n, int m, int lst, int fst) {
    if (n + m == kD) {
        if (fst == 0) {
            return used[0][0] ? kInf : Dp(n - 1, m, 0, 0);
        } else {
            return used[1][0] ? kInf : Dp(n, m - 1, 1, 1);
        }
    }
    if (n < 0 || m < 0) {
        return kInf;
    }
    if (n == 0 && m == 0) {
        return 0;
    }
    if (dp[n][m][lst][fst] == -1) {
        dp[n][m][lst][fst] = kInf;
        if (!used[0][kD - n - m]) {
            dp[n][m][lst][fst] = min(dp[n][m][lst][fst], (lst != 0) + Dp(n - 1, m, 0, fst) + (n + m == 1 && fst != 0));
        }
        if (!used[1][kD - n - m]) {
            dp[n][m][lst][fst] = min(dp[n][m][lst][fst], (lst != 1) + Dp(n, m - 1, 1, fst) + (n + m == 1 && fst != 1));
        }
    }
    return dp[n][m][lst][fst];
}


void Solve(int test_index) {
    memset(used, 0, sizeof(used));
    memset(dp, 255, sizeof(dp));
    int ac, aj;
    cin >> ac >> aj;
    for (int i = 0; i < ac; ++i) {
        int s, d;
        cin >> s >> d;
        for (int j = s; j < d; ++j) {
            used[0][j] = 1;
        }
    }
    for (int i = 0; i < aj; ++i) {
        int s, d;
        cin >> s >> d;
        for (int j = s; j < d; ++j) {
            used[1][j] = 1;
        }
    }
    int res = min(Dp(720, 720, 2, 0), Dp(720, 720, 2, 1));
    cout << "Case #" << test_index + 1 << ": " << res << '\n';
}

int main() {
    std::ios_base::sync_with_stdio(false);
    int tests_count;
    cin >> tests_count;
    for (int test_index = 0; test_index < tests_count; ++test_index) {
        Solve(test_index);
    }
    return 0;
}
