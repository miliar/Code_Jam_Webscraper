#include <cstdio>


using namespace std;

const int INF = 0x3f3f3f3f;
const int MAXN = 111;
int e[MAXN], d[MAXN][MAXN];
double s[MAXN], f[MAXN][MAXN];

int min(int a, int b) {
    return a < b ? a: b;
}

double min(double a, double b) {
    return a < b ? a: b;
}

int main() {
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int N, Q;
        scanf("%d%d", &N, &Q);
        for (int i = 1; i <= N; ++i) {
            scanf("%d%lf", &e[i], &s[i]);
        }
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                scanf("%d", &d[i][j]);
                if (d[i][j] == -1)
                    d[i][j] = INF; 
            }
            //d[i][i] = 0;
        }
        for (int k = 1; k <= N; ++k) {
            for (int i = 1; i <= N; ++i) {
                for (int j = 1; j <= N; ++j) {
                    d[i][j] = min(d[i][k] + d[k][j], d[i][j]);
                }
            }
        }
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                if (d[i][j] <= e[i]) 
                    f[i][j] = d[i][j] / s[i];
                else 
                    f[i][j] = 1e20;
            }
        }
        for (int k = 1; k <= N; ++k) {
            for (int i = 1; i <= N; ++i) {
                for (int j = 1; j <= N; ++j) {
                    f[i][j] = min(f[i][k] + f[k][j], f[i][j]);
                }
            }
        }
        printf("Case #%d: ", t);
        for (int i = 1; i <= Q; ++i) {
            int x, y;
            scanf("%d %d", &x, &y);
            printf("%.9lf", f[x][y]);
            if (i != Q)
                printf(" ");
        }
        printf("\n");
    }
    return 0;
} 