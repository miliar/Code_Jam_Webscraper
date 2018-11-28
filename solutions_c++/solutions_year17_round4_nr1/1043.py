#include <bits/stdc++.h>

using namespace std;

int F[105][105][105], n, p, cnt[5];

int solve() {
    memset(F, -1, sizeof F);
    F[0][0][0] = 0;
    for (int i = 0; i <= cnt[1]; ++i)
    for (int j = 0; j <= cnt[2]; ++j)
    for (int k = 0; k <= cnt[3]; ++k) {
        if (F[i][j][k]==-1) continue;
        int modNow = (i + 2*j + 3*k) % p;
        int add = 0;
        if (modNow==0) add = 1;
        if (i < cnt[1]) F[i+1][j][k] = max(F[i+1][j][k],F[i][j][k]+add);
        if (j < cnt[2]) F[i][j+1][k] = max(F[i][j+1][k],F[i][j][k]+add);
        if (k < cnt[3]) F[i][j][k+1] = max(F[i][j][k+1],F[i][j][k]+add);
    }
    return F[cnt[1]][cnt[2]][cnt[3]] + cnt[0];
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
    int t; scanf("%d",&t); int te = t;
    while (t--) {
        memset(cnt, 0, sizeof cnt);
        scanf("%d%d",&n,&p);
        for (int i = 0; i < n; ++i) {
            int x; scanf("%d",&x);
            cnt[x%p]++;
        }
        printf("Case #%d: %d\n",te-t,solve());
    }
	return 0;
}
