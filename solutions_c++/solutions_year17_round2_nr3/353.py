#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int n, q;
        scanf("%d %d", &n, &q);
        vector<long long> e(n);
        vector<long long> s(n);
        for (int i = 0; i < n; ++i) {
            scanf("%lld %lld", &e[i], &s[i]);
        }
        vector< vector<long long> > d(n);
        for (int i = 0; i < n; ++i) {
            d[i].resize(n);
            for (int j = 0; j < n; ++j) {
                scanf("%lld", &d[i][j]);
            }
        }

        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (d[i][k] != -1 && d[k][j] != -1) {
                        if (d[i][j] == -1 || d[i][j] > d[i][k] + d[k][j]) {
                            d[i][j] = d[i][k] + d[k][j];
                        }
                    }
                }
            }
        }

        printf("Case #%d:", t);
        for (int c = 0; c < q; ++c) {
            int u, v;
            scanf("%d %d", &u, &v);
            --u;
            --v;
            vector<double> be(n);
            vector<char> us(n);
            for (int j = 0; j < n; ++j) {
                be[j] = 1e20;
                us[j] = 0;
            }
            be[u] = 0;
            for (int i = 0; i < n; ++i) {
                int bj = 0;
                for (int j = 0; j < n; ++j) {
                    if (us[bj] && !us[j]) {
                        bj = j;
                    }
                    if (!us[j] && be[j] < be[bj]) {
                        bj = j;
                    }
                }
                if (us[bj]) {
                    break;
                }
                // printf("DEJ %d %lf\n", bj, be[bj]);
                us[bj] = 1;

                for (int j = 0; j < n; ++j) {
                // printf("DIST %d %d -> %lld\n", bj, j, d[bj][j]);
                    if (d[bj][j] != -1 && !us[j] && d[bj][j] <= e[bj]) {
                        be[j] = min(be[j], be[bj] + (double) d[bj][j] / s[bj]);
                    }
                }
            }
            printf(" %.7lf", be[v]);
        }
        printf("\n");
    }
    return 0;
}
