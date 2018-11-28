#include <iostream>
#include <vector>
#include <string>

using namespace std;


void run_testcase() {
    int n, q;
    cin >> n >> q;
    vector<vector<int64_t>> d(n, vector<int64_t>(n, -1));
    vector<int> e(n), s(n);
    for (int i = 0; i < n; ++i)
        cin >> e[i] >> s[i];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> d[i][j];
            if (d[i][j] == -1)
                d[i][j] = INT64_MAX / 1000LL;
            if (i == j)
                d[i][j] = 0;
        }
    }
    auto D = d;
    
    for (int k = 0; k < n; ++k)
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                D[i][j] = min (D[i][j], D[i][k] + D[k][j]);
    
    vector<vector<double>> g(n, vector<double>(n, INT64_MAX / 1000LL));
    
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (D[i][j] <= e[i])
                g[i][j] = (double)D[i][j] / (double)s[i];
    
    for (int k = 0; k < n; ++k)
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                g[i][j] = min (g[i][j], g[i][k] + g[k][j]);
    
    while (q--) {
        int a, b;
        cin >> a >> b;
        --a;--b;
        cout << fixed << g[a][b] << ' ';
    }
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cout.precision(10);
    freopen("/Users/nikita/Desktop/input.txt", "r", stdin);
    freopen("/Users/nikita/Desktop/output.txt", "w", stdout);
    
    // abcabcabc
    
    
    int Tcase;
    cin >> Tcase;
    for (int test = 1; test <= Tcase; ++test) {
        cout << "Case #" << test << ": ";
        run_testcase();
        cout << '\n';
    }
    
}
