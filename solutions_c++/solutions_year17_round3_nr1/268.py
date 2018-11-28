#include <bits/stdc++.h>
using namespace std;

const int maxn = 1010;
pair<int,int> p[maxn];
double dp[maxn][maxn];

const double pi = acos(-1.0);

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T, kase = 0;
	scanf("%d",&T);
	while (T--) {
		int n, k;
		scanf("%d%d",&n,&k);
		for (int i = 1; i <= n; i++) scanf("%d%d",&p[i].first,&p[i].second);
		sort(p+1,p+n+1);
		reverse(p+1,p+n+1);
		double ans = 0;
		memset(dp,0,sizeof(dp));
		for (int i = n; i >= 1; i--) {
			for (int j = 1; j <= k; j++) {
				dp[i][j] = max(dp[i][j],dp[i+1][j]);
				dp[i][j] = max(dp[i][j],dp[i+1][j-1]+2.0*pi*p[i].first*p[i].second);
			}
			ans = max(ans,dp[i+1][k-1]+pi*p[i].first*p[i].first+2.0*pi*p[i].first*p[i].second);
		}
		printf("Case #%d: %.10f\n",++kase,ans);
	}
	return 0;
}
