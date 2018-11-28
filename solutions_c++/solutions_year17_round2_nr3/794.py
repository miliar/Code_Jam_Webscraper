#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

const int MAXN = 110;
int n, q, T;
int d[MAXN][MAXN], e[MAXN], s[MAXN];
double f[MAXN];

int main(){
    cin >> T;
    for (int id = 1; id <= T; id++) {
        cin >> n >> q;
        printf("Case #%d:", id);
        for (int i = 0; i < n; i++) cin >> e[i] >> s[i];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                cin >> d[i][j];

        for (int i = 0; i < n; i++) d[i][i] = 0;
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (d[i][k] >= 0 && d[k][j] >= 0) {
                        int val = d[i][k] + d[k][j];
                        if (d[i][j] < 0 || d[i][j] > val) d[i][j] = val;
                    }

        while (q--) {
            int u, v;
            cin >> u >> v;
            u--;
            v--;

            for (int i = 0; i < n; i++) f[i] = 1e100;
            f[u] = 0;
            for (int k = 0; k < n; k++) {
                bool update = false;
                for (int i = 0; i < n; i++) {
                    if (f[i] == 1e100) continue;
                    for (int j = 0; j < n; j++) {
                        if (i == j) continue;
                        if (d[i][j] > 0 && d[i][j] <= e[i]) {
                            double val = f[i] + 1. * d[i][j] / s[i];
                            if (val < f[j]) {
                                f[j] = val;
                                update = true;
                            }
                        }
                    }
                }
                if (!update) break;
            }
            printf(" %.8f", f[v]);
        }
        cout << endl;
    }
}
