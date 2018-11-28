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
typedef long double ld;

void Solve(int test_index) {
    int n, k;
    cin >> n >> k;
    ld u;
    cin >> u;
    vector<ld> p(n);
    for (auto& x : p) { cin >> x; }
    ld l = 0.0, r = 1.0;
    const ld kEps = 1e-9;
    while (r - l > kEps) {
        ld uu = u;
        ld m = (l + r) / 2;
        vector<ld> pp = p;
        for (auto& x : pp) {
            if (x < m) {
                uu -= m - x;
                x = m;
            }
        }
        if (uu < -kEps) {
            r = m;
        } else {
            l = m;
        }
    }
    ld prob = 1.0;
    for (auto& x : p) {
        if (x < l) { x = l; }
        prob *= x;
    }
    cout.precision(10);
    cout << fixed << "Case #" << test_index + 1 << ": " << (double) prob << '\n';
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
