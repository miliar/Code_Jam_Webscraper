#include <bits/stdc++.h>

using namespace std;

#define int long long

template<typename T>
void floyd(vector< vector<T> > &d) {
    int n = d.size();
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (d[i][k] == -1 || d[k][j] == -1) continue;
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
                if (d[i][j] == -1) d[i][j] = d[i][k] + d[k][j];
            }
        }
    }
}

void solve(int test) {
    int n, q;
    cin >> n >> q;
    vector<int> maxdist(n);
    vector<int> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> maxdist[i] >> s[i];
    }
    vector< vector<int> > d(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> d[i][j];
            if (i == j) d[i][j] = 0;
        }
    }
    floyd(d);
    vector< vector<double> > dd(n, vector<double>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            dd[i][j] = d[i][j];
            if (d[i][j] > maxdist[i]) dd[i][j] = -1;
            if (dd[i][j] == -1) continue;
            dd[i][j] /= s[i];
        }
    }
    floyd(dd);

    cout << "Case #" << test << ": ";
    for (int i = 0; i < q; ++i) {
        int a, b;
        cin >> a >> b;
        --a; --b;
        cout << dd[a][b] << ' ';
    }
    cout << '\n';

}

signed main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false); cin.tie(0);
    cout << fixed; cout.precision(12);

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
}
