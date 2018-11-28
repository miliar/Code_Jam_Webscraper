#include <bits/stdc++.h>
#define ll long long
#define mst(a,x) memset(a,x,sizeof(a))
#define For(i, t) for(int i = 0; i < t; i++)
#define Debug(x) cerr << #x << " = "  << x << endl;
using namespace std;

const int N = 105;
const int INF = 1e9;
int dp[N][N][N], n, p, a[N], cnt[5];
int main() {
    int T, n, k;

    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    For(cas, T) {
        scanf("%d%d", &n, &p);
        mst(cnt, 0);
        int sum = 0;
        For(i, n) {
            scanf("%d", a + i);
            sum += a[i];
            cnt[a[i] % p]++;
        }
        for(int a = cnt[1]; ~a; a--)
            for(int b = cnt[2]; ~b; b--)
                for(int c = cnt[3]; ~c; c--) 
                    dp[a][b][c] = -INF;

        //printf("cnt %d %d %d\n", cnt[1], cnt[2], cnt[3]);
        dp[cnt[1]][cnt[2]][cnt[3]] = cnt[0];
        for(int a = cnt[1]; ~a; a--)
            for(int b = cnt[2]; ~b; b--)
                for(int c = cnt[3]; ~c; c--) {
                    int cur = dp[a][b][c];
                    if(cur == -INF) continue;
                    int left = sum - a * 1 - b * 2 - c * 3;
                    left %= p;
                    int add = left == 0 ? 1 : 0;
                    if(a) 
                        dp[a - 1][b][c] = max(dp[a - 1][b][c], cur + add);
                    if(b)
                        dp[a][b - 1][c] = max(dp[a][b - 1][c], cur + add);
                    if(c)
                        dp[a][b][c - 1] = max(dp[a][b][c - 1], cur + add);
                }

        printf("Case #%d: %d\n", cas + 1, dp[0][0][0]);
    }
	return 0;
}
