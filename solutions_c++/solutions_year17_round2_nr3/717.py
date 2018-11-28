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

const long long INF = 1e18;

double solveOne(int n, const vector<long long>& e, const vector<long long>& s, const vector<vector<long long> >& d, int u, int v) {
    set<pair<double, int> > q;
    q.insert(make_pair(0, u));

    double ans = INF;
    vector<bool> used(n, false);
    while (!q.empty()) {
        int cur = q.begin()->second;
        double t = q.begin()->first;
        q.erase(q.begin());

        if (cur == v) {
            ans = min(ans, t);
        }

        used[cur] = true;
        for (int i = 0; i < n; ++i) {
            if (!used[i] && e[cur] >= d[cur][i]) {
                q.insert(make_pair(t + 1.0 * d[cur][i] / s[cur], i));
            }
        }
    }

    return ans;
}

void solve() {
    int n, q;
    cin >> n >> q;

    vector<long long> e(n), s(n);
    for (int i = 0; i < n; ++i) {
        cin >> e[i] >> s[i];
    }

    vector<vector<long long> > d(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> d[i][j];
            if (d[i][j] < 0) {
                d[i][j] = INF;
            }
        }
    }
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }

    const long long INF = 1e18;
    for (int qq = 0; qq < q; ++qq) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        printf("%.6lf ", solveOne(n, e, s, d, u, v));
    }
    cout << endl;
}

int main() {
    freopen("C-large.in", "r", stdin);
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
