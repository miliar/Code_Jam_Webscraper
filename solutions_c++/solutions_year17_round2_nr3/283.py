#include <bits/stdc++.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define sz(v) int(v.size())

using namespace std;

typedef long long ll;

ll dst[105][105];
double dst2[105][105];
ll md[105]; double sp[105];
int n, q;

int main() {
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        scanf("%d %d", &n, &q);
        FO(i,0,n) FO(j,0,n) dst[i][j] = i == j ? 0 : 1e18;
        FO(i,0,n) {
            scanf("%lld %lf", &md[i], &sp[i]);
        }
        FO(i,0,n) FO(j,0,n) {
            ll d; scanf("%lld", &d);
            if (d != -1) {
                dst[i][j] = min(dst[i][j], d);
            }
        }
        FO(i,0,n) FO(j,0,n) FO(k,0,n) dst[j][k] = min(dst[j][k], dst[j][i]+dst[i][k]);
        FO(i,0,n) FO(j,0,n) dst2[i][j] = i == j ? 0 : 1e18;
        FO(i,0,n) FO(j,0,n) if (md[i] >= dst[i][j]) {
            dst2[i][j] = min(dst2[i][j], dst[i][j] / sp[i]);
        }
        FO(i,0,n) FO(j,0,n) FO(k,0,n) dst2[j][k] = min(dst2[j][k], dst2[j][i]+dst2[i][k]);
        printf("Case #%d:", Z);
        FO(i,0,q) {
            int u, v; scanf("%d %d", &u, &v); u--; v--;
            printf(" %.9lf", dst2[u][v]);
        }
        printf("\n");
    }
}
