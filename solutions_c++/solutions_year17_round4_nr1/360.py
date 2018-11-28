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

const int kN = 100 + 1;
const int kP = 4;
const int kInf = 1e9;

int n, p;
int dp[kP][kN][kN][kN][kN];

int Dp(int sum, int k0, int k1, int k2, int k3) {
    if (k0 < 0 || k1 < 0 || k2 < 0 || k3 < 0) {
        return -kInf;
    }
    if (k0 + k1 + k2 + k3 == 0) {
        return 0;
    }
    if (dp[sum][k0][k1][k2][k3] == -1) {
        int inc = sum == 0;
        int& res = dp[sum][k0][k1][k2][k3];
        res = -kInf;
        res = max(res, inc + Dp(sum, k0 - 1, k1, k2, k3));
        res = max(res, inc + Dp((sum + 1) % p, k0, k1 - 1, k2, k3));
        res = max(res, inc + Dp((sum + 2) % p, k0, k1, k2 - 1, k3));
        res = max(res, inc + Dp((sum + 3) % p, k0, k1, k2, k3 - 1));
    }
    return dp[sum][k0][k1][k2][k3];
}

void Solve(int test_index) {
    cin >> n >> p;
    vector<int> arr(n);
    vector<int> cnt(kN);
    for (int& x : arr) { cin >> x; ++cnt[x % p]; }
    memset(dp, 255, sizeof(dp));
    int res = Dp(0, cnt[0], cnt[1], cnt[2], cnt[3]);
    cerr << "test_index: " << test_index << endl;
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
