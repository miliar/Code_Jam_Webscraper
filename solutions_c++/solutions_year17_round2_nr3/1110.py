#include <cstdio>
#include <iostream>

using namespace std;

int e[111], s[111];
int d[111][111];
double ans[111];

int main()
{
    int T;
    cin >> T;
    for (int tt = 1; tt <= T; tt++)
    {
        int n, Q; cin >> n >> Q;
        for (int i = 0; i < n; i++) {
            cin >> e[i] >> s[i];
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> d[i][j];
            }
        }

        for (int q = 0; q < Q; q++) {
            int u, v; cin >> u >> v;
            for (int i = 0; i < 111; i++) ans[i] = 1e18;
            // 0 > n -1
            ans[0] = 0;
            for (int i = 0; i < n - 1; i++) {
                long long di = 0;
                for (int j = i + 1; j < n; j++) {
                    di += d[j-1][j];
                    if (di > e[i]) {
                        break;
                    }

                    double time = (double)di / s[i];
                    if (ans[j] > ans[i] + time) {
                        ans[j] = ans[i] + time;
                    }
                }
            }
        }


        printf("Case #%d: %.8lf\n", tt, ans[n-1]);
    }

    return 0;
}
