#include <cstdio>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long long ll;

const int MAXN = 200;
const ll INF = 1000LL * 1000 * 1000 * 1000 * 1000 * 1000;

ll d[MAXN][MAXN];
double g[MAXN][MAXN];
ll e[MAXN], s[MAXN];

int main() {
    int testCases;
    cin >> testCases;

    for (int testCase = 1; testCase <= testCases; testCase++) {
        int n, q;
        cin >> n >> q;

        for (int i = 1; i <= n; i++) {
            cin >> e[i] >> s[i];
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cin >> d[i][j];
                if (d[i][j] == -1) {
                    d[i][j] = INF;
                }
            }
        }

        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                g[i][j] = INF * 1.0;

                if (d[i][j] != INF && d[i][j] <= e[i]) {
                    g[i][j] = d[i][j] * 1.0 / s[i];
                    //cout << d[i][j] << " " << s[i] << " = " << g[i][j] << endl;
                }
            }
        }

        
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
                }
            }
        }
        
        /*
        cout << endl;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cout << d[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cout << fixed << setprecision(3) << g[i][j] << " ";
            }
            cout << endl;
        }
        */


        cout << "Case #" << testCase << ": ";

        for (int i = 0; i < q; i++) {
            int x, y;
            cin >> x >> y;
            cout << fixed << setprecision(9) << g[x][y] << " ";
        }

        cout << endl;
    }
}
