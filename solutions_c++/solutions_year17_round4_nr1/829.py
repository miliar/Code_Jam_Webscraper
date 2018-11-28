#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>

using namespace std;

void precalc() {

}

void solve() {
    int n, p;
    cin >> n >> p;

    vector<int> v(p);
    for (int i = 0; i < n; ++i) {
        int t;
        cin >> t;
        ++v[t % p];
    }

    int res = 0;
    if (p == 2) {
        res = n - (v[1] / 2);
    } else if (p == 3) {
        int b = min(v[1], v[2]);
        res = b;
        v[1] -= b;
        v[2] -= b;
        res += v[1] / 3;
        v[1] %= 3;
        res += v[2] / 3;
        v[2] %= 3;
        res += v[0];
        if (v[1] > 0 || v[2] > 0) ++res;
    } else {
        int b = min(v[1], v[3]);
        res = b;
        v[1] -= b;
        v[3] -= b;
        res += v[2] / 2;
        v[2] %= 2;
        if (v[2] > 0 && v[1] > 1) {
            ++res;
            --v[2];
            v[1] -= 2;
        }
        res += v[1] / 4;
        v[1] %= 4;
        res += v[2] / 4;
        v[2] %= 4;
        res += v[3] / 4;
        v[3] %= 4;
        res += v[0];
        if (v[1] > 0 || v[2] > 0 || v[3] > 0) ++res;
    }
    cout << res << endl;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    precalc();

    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": ";
        cerr << test << endl;
        solve();
    }
    return 0;
}
