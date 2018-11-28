#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const long double INF = 1e18;

void solve() {
    int n, q;
    cin >> n >> q;
    vector<int> e(n), s(n);
    for (int i = 0; i < n; i++) {
        cin >> e[i] >> s[i];
    }
    vector<vector<int> > d(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> d[i][j];
        }
    }
    int v1, v2;
    for (int i = 0; i < q; i++)
        cin >> v1 >> v2;
    vector<long double> f(n);
    f[n - 1] = 0;
    for (int i = n - 2; i >= 0; i--) {
        if (e[i] < d[i][i + 1]) {
            f[i] = INF;
        } else {
            long double curd = 0;
            f[i] = INF;
            for (int j = i + 1; j < n; j++) {
                curd += d[j - 1][j];
                if (curd <= e[i]) {
                    f[i] = min(f[i], curd / s[i] + f[j]);
                }
            }
        }
    }
    cout.precision(10);
    cout << fixed << f[0] << endl;
}

int main() {
    int cntTests;
    cin >> cntTests;
    for (int curTest = 0; curTest < cntTests; curTest++) {
        cout << "Case #" << curTest + 1 << ": ";
        solve();
    }
}