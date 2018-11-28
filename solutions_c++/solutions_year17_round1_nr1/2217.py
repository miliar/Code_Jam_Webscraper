#include <bits/stdc++.h>

using namespace std;

int main() {
//    freopen("sample.in", "r", stdin);
//    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    for (int ti = 1; ti <= tc; ++ti) {
        cout << "Case #" << ti << ":\n";
        int n, m;
        cin >> n >> m;
        vector<string> rs(n);
        int gl = -1, lg = -1;
        for (int i = 0; i < n; ++i) {
            cin >> rs[i];
            bool ok = false;
            for (int j = 0; j < m; ++j)
                if (rs[i][j] != '?') {
                    ok = true;
                    break;
                }
            if (ok) {
                if (gl == -1) {
                    gl = i;
                }
                lg = i;
            }
            else if (lg != -1) {
                rs[i] = rs[lg];
            }
        }
        for (int i = 0; i < gl; ++i) 
            rs[i] = rs[gl];
        for (int i = 0; i < n; ++i) {
            gl = -1; lg = -1;
            for (int j = 0; j < m; ++j) {
                if (rs[i][j] != '?') {
                    if (gl == -1)
                        gl = j;
                    lg = j;
                }
                else if (lg != -1) {
                    rs[i][j] = rs[i][lg];
                }
            }
            for (int j = 0; j < gl; ++j) {
                rs[i][j] = rs[i][gl];
            }
            cout << rs[i] << "\n";
        }
    }
    return 0;
}
