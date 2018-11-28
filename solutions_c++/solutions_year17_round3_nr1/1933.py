#include <bits/stdc++.h>
#define N 1005
using namespace std;
#define fi first
#define se second
int n,k;
pair<int,int> a[N];
double dp[N][N];
int main(){
	freopen("A-large.in","r",stdin); freopen("A.out","w",stdout);
	int t; scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		scanf("%d %d",&n,&k);
		for(int i=1;i<=n;i++) scanf("%d %d",&a[i].fi,&a[i].se);
		sort(a+1,a+n+1,greater< pair<int, int> >() );
		memset(dp,0,sizeof(dp));
		double ans=0.0;
		for(int i=1;i<=n;i++){
			for(int j=1;j<=i;j++){
				if (j==1) dp[i][j] = max(dp[i-1][j],(double)a[i].fi * a[i].fi * M_PI + 2.0 * a[i].fi * a[i].se * M_PI); 
				else dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + 2.0 * M_PI * a[i].fi * a[i].se);
			}
			if (i>=k) ans=max(ans,dp[i][k]);
		}
		printf("Case #%d: %.7lf\n",tc,ans);
	}
}
/*
input:
1
6 2
17913 30
16758 72
3929 373187
3311 336351
3295 354362
3245 364565

output:
Case #1: 16694320747.335318
*/
