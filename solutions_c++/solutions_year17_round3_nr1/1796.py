#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const double pi = acos(0.0) * 2;
long long dp[1010][1010];

struct cake {
    long long r;
    long long h;
    bool operator < (const cake &a) const {
        return r < a.r;
    }
}o[1010];

int main() {
    int t, tc;
    int i, j, n, k;
    long long ans;
    freopen("/Users/SeoByeongChan/Downloads/input.txt","rt",stdin);
    freopen("/Users/SeoByeongChan/Downloads/output.txt","w",stdout);
    scanf("%d",&t);
    for(tc = 1; tc <= t; tc++) {
        scanf("%d %d",&n,&k);
        for(i=0;i<n;i++) for(j=0;j<=k;j++) dp[i][j] = 0;
        for(i=0;i<n;i++) scanf("%lld %lld",&o[i].r,&o[i].h);
        sort(o, o + n);
        dp[0][1] = o[0].r * o[0].h * 2;
        ans = o[0].r * o[0].h * 2 + o[0].r * o[0].r;
        for(i=1;i<n;i++) {
            for(j=0;j<k;j++) {
                dp[i][j+1] = dp[i-1][j] + o[i].r * o[i].h * 2;
                if(dp[i][j+1] + o[i].r * o[i].r > ans) ans = dp[i][j+1] + o[i].r * o[i].r;
            }
            for(j=0;j<=k;j++) dp[i][j] = max(dp[i][j], dp[i-1][j]);
        }
        printf("Case #%d: %.6lf\n",tc, ans*pi);
    }
    return 0;
}
