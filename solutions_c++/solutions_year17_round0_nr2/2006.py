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

ll GetMinNumber(ll pref, int dig, int cnt) {
    for (int i = 0; i < cnt; ++i) {
        pref = pref * 10 + dig;
    }
    return pref;
}

void Solve(int test_index) {
    ll n;
    cin >> n;
    const int kN = 19;
    ll res = 0;
    for (int i = 0; i < kN; ++i) {
        int dig = 0;
        while (dig < 9 && GetMinNumber(res, dig + 1, kN - i) <= n) {
            ++dig;
        }
        res = res * 10 + dig;
    }
    cout << "Case #" << test_index << ": " << res << "\n";
}

int main() {
    std::ios_base::sync_with_stdio(false);
    int tests_count;
    cin >> tests_count;
    for (int test_index = 0; test_index < tests_count; ++test_index) {
        Solve(test_index + 1);
    }
    return 0;
}
