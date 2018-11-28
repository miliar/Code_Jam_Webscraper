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

pair<int, int> solveDummy(const vector<vector<int> >& v) {
    int res = 0, prom = 0;

    int fr = 0, sr = 0;
    for (int i = 0; i < v.size(); ++i) {
        fr += v[i][0];
        sr += v[i][1];
    }

    res = max(max(fr, sr), v[0][0] + v[0][1]);
    for (int i = 0; i < v.size(); ++i) {
        int sm = v[i][0] + v[i][1];
        if (sm > res) {
            prom += sm - res;
        }
    }

    return make_pair(res, prom);
}

void solve() {
    int n, c, m;
    cin >> n >> c >> m;

    vector<vector<int> > v(n, vector<int>(c, 0));
    for (int i = 0; i < m; ++i) {
        int p, b;
        cin >> p >> b;
        --p;
        --b;
        ++v[p][b];
    }

    auto res = solveDummy(v);
    cout << res.first << " " << res.second << endl;
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
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
