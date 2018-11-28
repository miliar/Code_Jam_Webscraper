#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int E[1000], S[1000], D[1000][1000];

int answered[1000]; double mem[1000];
double ans(int pos, int N) {
    if (answered[pos])
        return mem[pos];
    if (pos == N-1)
        return 0;
    int i; ll d = 0; double res = -1.0, tmp;
    for(i=pos+1;i<N;i++) {
        d += D[i-1][i];
        if (d > E[pos]) break;
        tmp = ans(i, N);
        if (tmp < 0) continue;
        tmp += (double)d / S[pos];
        if (res < 0 || tmp < res)
            res = tmp;
    }
    answered[pos] = 1;
    return mem[pos] = res;
}

int main() {

    // freopen("C-small-attempt0.in", "r", stdin);
    // freopen("C-small-attempt0.out", "w", stdout);

    int T, k = 0, N, Q, i, u, v, j;

    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++k);
        scanf("%d%d", &N, &Q);
        for(i=0;i<N;i++)
            scanf("%d%d", &E[i], &S[i]);
        for(i=0;i<N;i++)
            for(j=0;j<N;j++)
                scanf("%d", &D[i][j]);
        scanf("%d%d", &u, &v);
        memset(answered, 0, sizeof(answered));
        printf("%.7f\n", ans(0, N));
    }

    return 0;
}
