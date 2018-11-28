#include<bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 5;
long long dp[100][100];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    int T; scanf("%d",&T);
    for(int cas = 1; cas <= T; cas ++) {
        int d, n; scanf("%d%d", &d, &n);
        double ans = d;int flag = 0;
        for(int i = 0, k, x; i < n; i ++) {
            scanf("%d%d", &k, &x);
            if (!flag) {
                ans = d * 1.0 * x / (d - k);
                flag = 1;
            }
            else{
                ans = min(ans, d * 1.0 * x / (d - k));
            }

        }
        printf("Case #%d: %.10f\n", cas, ans);
    }
    return 0;
}
