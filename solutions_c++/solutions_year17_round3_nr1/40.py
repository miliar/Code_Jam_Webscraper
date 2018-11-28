#include <bits/stdc++.h>
#define ll long long
#define mst(a,x) memset(a,x,sizeof(a))
#define For(i, t) for(int i = 0; i < t; i++)
#define Debug(x) cerr << #x << " = "  << x << endl;
using namespace std;


const int N = 1005;
const double pi = acos(-1.0);

struct Cake{
    int r, h;
    void Read() {
        scanf("%d%d", &r, &h);
    }
    bool operator < (const Cake &b)const{
        return r > b.r;
    }
}a[N];
double dp[N][N];

int main() {
    int T, n, k;

    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    For(cas, T) {
        mst(dp, 0);
        scanf("%d%d", &n, &k);
        for(int i = 1; i <= n; i++) a[i].Read();
        sort(a + 1, a + 1 + n);
        //printf("%.10f\n", 2 * pi * a[1].r * a[1].h + pi * a[1].r * a[1].r);
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= k; j++) {
                dp[i][j] = dp[i - 1][j];
                if(j == 1) dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 2 * pi * a[i].r * a[i].h + pi * a[i].r * a[i].r);
                else dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 2 * pi * a[i].r * a[i].h);
            }
        printf("Case #%d: %.10f\n", cas + 1, dp[n][k]);
    }
	return 0;
}
