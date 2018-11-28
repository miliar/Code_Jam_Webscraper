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

const double EPS = 1e-6;

void precalc() {
}

void solve() {
    long long d, n;
    cin >> d >> n;

    vector<pair<long long, long long> > v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i].first >> v[i].second;
    }

    sort(v.begin(), v.end());

    vector<double> t(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
        double S = d - v[i].first;
        double V = v[i].second;

        if (i == n - 1 || S / V + EPS >= t[i + 1]) {
            t[i] = S / V;
        } else {
            t[i] = t[i + 1];
        }
    }

    printf("%.6lf\n", d / t[0]);
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
