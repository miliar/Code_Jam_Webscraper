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
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;

    vector<pair<int, char> > a(3);
    a[0] = make_pair(r, 'R');
    a[1] = make_pair(y, 'Y');
    a[2] = make_pair(b, 'B');

    string s(n, '0');
    for (int i = 0; i < n; ++i) {
        sort(a.begin(), a.end());
        reverse(a.begin(), a.end());
        for (int j = 0; j < 3; ++j) {
            if (a[j].first > 0 && (i == 0 || s[i - 1] != a[j].second)) {
                s[i] = a[j].second;
                --a[j].first;
                break;
            }
        }
    }

    bool ok = true;
    if (s[0] == s.back()) {
        swap(s[s.size() - 1], s[s.size() - 2]);
    }
    if (s[0] == s.back() || s[0] == '0') {
        ok = false;
    }
    for (int i = 1; i < n && ok; ++i) {
        if (s[i] == s[i - 1] || s[i] == '0') {
            ok = false;
        }
    }

    if (!ok) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << s << endl;
    }
}

int main() {
    freopen("B-small-attempt1.in", "r", stdin);
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
