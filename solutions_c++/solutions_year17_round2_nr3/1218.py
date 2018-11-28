#include <bits/stdc++.h>

using namespace std;

int n, t, w = 1, q, u, v;

long double e[100], s[100], g[100][100], d[100], m[100];

int main() {
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    while(w <= t){
        cout << "Case #" << w << ": ";
        ++w;
       cin >> n >> q;
        for(int i = 0; i < n; ++i){
            cin >> e[i] >> s[i];
        }
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                cin >> g[i][j];
            }
        }
        cin >> u >> v;
        for(int i = n - 2; i >= 0; --i){
            d[i] = g[i][i + 1] + d[i + 1];
        }
        for(int i = 1; i < n; ++i){
            m[i] = 100000000000.0;
        }
        for(int i = 0; i < n; ++i){
            for(int j = i + 1; j < n; ++j){
                if(d[i] - d[j] > e[i]){
                    break;
                }
                m[j] = min(m[j], m[i] + (d[i] - d[j]) / s[i]);
            }
        }
        cout << fixed;
        cout << setprecision(12) << m[n - 1] << "\n";
    }
    return 0;
}