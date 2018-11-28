#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define PROBLEM "C-small-attempt1"

using namespace std;

void solve(int n, int q) {
    vector<int> e(n), s(n), d(n);
    for (int i = 0; i < n; ++i) {
        cin >> e[i] >> s[i];
    }
    for (int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            int a;
            cin >> a;
            if (a != -1) {
                d[i] = a;
            }
        }
    }
    int u, v;
    cin >> u >> v;
    if (q != 1 || u != 1 || v != n) {
        cerr << "Error! q = " << q << "  u = " << u << "  v = " << v << endl;
        throw "wtf";
    }
    vector<double> t(n);
    t[n-1] = 0;
    for (int i = n-2; i >= 0; --i) {
        double &b = t[i];
        b = 2e12;
        long long ss = d[i];
        for (int j = i + 1; j < n; ++j) {
            if (ss > e[i]) break;
            b = min(b, t[j] + (ss / (double) s[i]));
            ss += d[j];
        }
    }
    cout << " ";
    cout.precision(6);
    cout << fixed << t[0];
}

int main()
{
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int q, n;
        cin >> n >> q;
        cout << "Case #" << t << ":";
        solve(n, q);
        cout << endl;
    }
    return 0;
}
