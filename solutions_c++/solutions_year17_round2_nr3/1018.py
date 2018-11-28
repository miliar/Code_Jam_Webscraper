#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn = 110;
int E[maxn], S[maxn], D[maxn][maxn];
double f[maxn];

int main() {
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ca++) {
        int N, Q;
        scanf("%d%d", &N, &Q);
        for (int i = 1; i <= N; i++) scanf("%d%d", &E[i], &S[i]);
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                scanf("%d", &D[i][j]);
            }
        }
        while (Q--) {
            int U, V;
            scanf("%d%d", &U, &V);
            for (int i = 2; i <= N; i++) f[i] = 1e18;
            f[1] = 0;
            for (int i = 1; i <= N; i++) {
                int x = E[i], pos = i + 1;
                double t = f[i];
                while (x >= 0 && pos <= N) {
                    x -= D[pos - 1][pos];
                    if (x >= 0) {
                        t += 1.0 * D[pos - 1][pos] / S[i];
                        f[pos] = min(f[pos], t);
                    }
                    pos++;
                }
            }
            printf("Case #%d: %.8lf\n", ca, f[N]);
        }
    }
    return 0;
}