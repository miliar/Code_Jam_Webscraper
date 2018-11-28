#include <iostream>
#include <cstdio>
#include <cstring> // memset
#include <algorithm> // sort
#include <queue>
using namespace std;

double e[120], s[120];
double d[120][120];
double t[120];
int main() {
    int T;
    cin >> T;
    for (int ii = 1; ii <= T; ii++) {
        int n, q;
        cin >> n >> q;
        for (int i = 0; i < n; i++) {
            cin >> e[i] >> s[i];
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> d[i][j];
                if (d[i][j] < 0) 
                    d[i][j] = 10e20+20;
            }
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (d[i][j] > d[i][k] + d[k][j])
                        d[i][j] = d[i][k] + d[k][j];
                }
            }
        }
        cout << "Case #" << ii << ":";
        for (int i = 0; i < q; i++) {
            int u, v;
            cin >> u >> v;
            queue<int> qu;
            u -= 1;
            v -= 1;
            for (int j = 0; j < n; j++) {
                t[j] = 10e20+20;
            }
            t[u] = 0;
            qu.push(u);
            while (!qu.empty()) {
                int m = qu.front();
                qu.pop();
                for (int j = 0; j < n; j++) {
                    if (d[m][j] <= e[m] && t[j] > t[m] + d[m][j]/s[m]){
                        t[j] = t[m] + d[m][j]/s[m];
                        qu.push(j);
                    }
                }
            }
            printf(" %.6f", t[v]);
        }
        cout << endl;
    }
    return 0;
}
