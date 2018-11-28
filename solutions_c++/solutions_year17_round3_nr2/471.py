#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

double P[55];

pair<int, int> a[105], b[105];
int A[1445];
int F[1445][725], G[1445][725];

int main() {
    freopen("B.in", "r", stdin);
    freopen("B_large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++) {
        int n, m;
        cin >> n >> m;
        int l, r;
        memset(A, 0, sizeof(A));
        memset(F, -1, sizeof(F));
        memset(G, -1, sizeof(G));
        for(int i = 0; i < n; i ++) {
            cin >> l >> r;
            for(int j = l; j < r; j ++) A[j] = 1;
        }
        for(int i = 0; i < m; i ++) {
            cin >> l >> r;
            for(int j = l; j < r; j ++) A[j] = 2;
        }
        printf("Case #%d: ", kase);

        int ped = 0;
        for(int i = 0; i < 1440; i ++) if(A[i] == 0) ped ++; else break;
        for(int i = ped; i < 1440; i ++) {
            A[i-ped] = A[i];
        }
        for(int i = 1440 - ped; i < 1440; i ++) {
            A[i] = 0;
        }
        if(A[0] == 2) {
            for(int i = 0; i < 1440; i ++) {
                if(A[i] == 1) A[i] = 2;
                else if(A[i] == 2) A[i] = 1;
            }
        }

        F[1][1] = 0;
        G[1][0] = 1;
        for(int i = 2; i <= 1440; i ++) {
            for(int j = 1; j <= 720; j ++) {
                if(A[i-1] != 2) {
                    int now = 1000000;
                    if(F[i-1][j-1] != -1 && F[i-1][j-1] < now) {
                        now = F[i-1][j-1];
                    }
                    if(G[i-1][j-1] != -1 && G[i-1][j-1]+1 < now) {
                        now = G[i-1][j-1] + 1;
                    }
                    if(now != 1000000) F[i][j] = now;
                }
            }
            for(int j = 0; j <= 720; j ++) {
                if(A[i-1] != 1) {
                    int now = 1000000;
                    if(F[i-1][j] != -1 && F[i-1][j]+1 < now) {
                        now = F[i-1][j] + 1;
                    }
                    if(G[i-1][j] != -1 && G[i-1][j] < now) {
                        now = G[i-1][j];
                    }
                    if(now != 1000000) G[i][j] = now;
                }
            }
        }

        int ans = 1000000;
        if(F[1440][720] != -1) ans = F[1440][720];
        if(G[1440][720] != -1 && G[1440][720] + 1 < ans) ans = G[1440][720] + 1;
        if(ans == 1000000) printf("error!\n");
        printf("%d\n", ans);
    }
    return 0;
}

