#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int G[100], F[100];

int main() {

    // freopen("A-small-attempt0.in", "r", stdin);
    // freopen("A-small-attempt0.out", "w", stdout);

    int T, k = 0, i, j, l, m, P, N, ans;

    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++k);
        scanf("%d%d", &N, &P);
        memset(F, 0, sizeof(F));
        for(i=0;i<N;i++)
            scanf("%d", &G[i]);
        ans = 0;
        for(i=0;i<N;i++)
        if (G[i] % P == 0) {
            ans++;
            F[i] = 1;
        }
        for(i=0;i<N;i++) {
            if (F[i] == 0) {
                for(j=i+1;j<N;j++) {
                    if (F[j] == 0 && (G[j]+G[i])%P == 0) {
                        ans++;
                        F[j] = 1;
                        F[i] = 1;
                        break;
                    }
                }
            }
        }
        for(m=0;m<N;m++) {
            for(i=m+1;i<N&&!F[m];i++) {
                for(j=i+1;j<N&!F[i];j++) {
                    if (F[j] == 0 && (G[m]+G[j]+G[i])%P == 0) {
                        ans++;
                        F[j] = 1;
                        F[i] = 1;
                        F[m] = 1;
                    }
                }
            }
        }
        for(l=0;l<N;l++) {
            for(m=0;m<N&&!F[l];m++) {
                for(i=m+1;i<N&&!F[m];i++) {
                    for(j=i+1;j<N&!F[i];j++) {
                        if (F[j] == 0 && (G[m]+G[j]+G[i])%P == 0) {
                            ans++;
                            F[j] = 1;
                            F[i] = 1;
                            F[m] = 1;
                            F[l] = 1;
                        }
                    }
                }
            }
        }
        for(i=0;i<N&&F[i];i++);
        if (i < N) ans++;
        printf("%d\n", ans);
    }

    return 0;
}
