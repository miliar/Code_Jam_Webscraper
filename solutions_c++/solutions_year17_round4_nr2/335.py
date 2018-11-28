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

int a[kN][kN];
int sums[kN], rows[kN];

bool Check(int n, int sum) {
    int row_max = *max_element(rows, rows + kN);
    if (row_max > sum) { return false; }
    int carry = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (sums[i] >= sum) {
            carry += sums[i] - sum;
        } else {
            carry -= sum - sums[i];
            carry = max(carry, 0);
        }
    }
    return carry == 0;
}

int F(int n) {
    int l = 0, r = kN;
    while (l < r) {
        int m = (l + r) >> 1;
        if (!Check(n, m)) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    return l;
}


void Solve(int test_index) {
    memset(a, 0, sizeof(a));
    memset(rows, 0, sizeof(rows));
    memset(sums, 0, sizeof(sums));
    int n, k, m;
    cin >> n >> k >> m;
    while (m--) {
        int pos, id;
        cin >> pos >> id;
        ++a[id - 1][pos - 1];
    }
    for (int row = 0; row < k; ++row) {
        for (int col = 0; col < n; ++col) {
            rows[row] += a[row][col];
            sums[col] += a[row][col];
        }
    }
    int res = F(n);
    int ans = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (sums[i] >= res) {
            ans += sums[i] - res;
        }
    }
    cout << "Case #" << test_index + 1 << ": " << res << ' ' << ans << '\n';
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
