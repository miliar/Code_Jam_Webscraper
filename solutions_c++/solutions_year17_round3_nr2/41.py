#include <bits/stdc++.h>
#define ll long long
#define mst(a,x) memset(a,x,sizeof(a))
#define For(i, t) for(int i = 0; i < t; i++)
#define Debug(x) cerr << #x << " = "  << x << endl;
using namespace std;


const int INF = 1e9 + 5;
const int D = 1440;
int dp[D + 5][D / 2 + 5][2], n, m, flag[D + 5];
int ans;

void work(int s) {
    if(~flag[1] && flag[1] != s) return;
    mst(dp, 0x3f);
    if(s == 0) {
        dp[1][1][0] = 0;
    }else {
        dp[1][0][1] = 0;
    }

    for(int i = 1; i < D; i++) {
        for(int j = 0; j <= D / 2; j++) {
            for(int k = 0; k < 2; k++) {
                int pre = dp[i][j][k];
                if(pre > INF) continue;
                for(int t = 0; t < 2; t++) {
                    if(~flag[i + 1] && t != flag[i + 1]) continue;
                    int diff = (k == t ? 0 : 1);
                    if(t == 0 && j < D / 2) {
                        dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], pre + diff);
                    }
                    if(t == 1) {
                        dp[i + 1][j][1] = min(dp[i + 1][j][1], pre + diff);
                    }
                }
            }
        }
    }
    For(i, 2) {
        int diff = i == s ? 0 : 1;
        ans = min(ans, dp[D][D / 2][i] + diff);
    }
}

int main() {
    int T;

    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    For(cas, T) {
        int n, m, l, r;
        mst(flag, -1);
        scanf("%d%d", &n, &m);
        For(i, n) {
            scanf("%d%d", &l, &r);
            for(int j = l + 1; j <= r; j++) 
                flag[j] = 0;
        }

        For(i, m) {
            scanf("%d%d", &l, &r);
            for(int j = l + 1; j <= r; j++) 
                flag[j] = 1;
        }

        ans = D * 2;
        For(i, 2) work(i);
        printf("Case #%d: %d\n", cas + 1, ans);
    }
	return 0;
}
