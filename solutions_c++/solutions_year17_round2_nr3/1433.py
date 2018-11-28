#include <bits/stdc++.h>
using namespace std;

int t;

int main(){
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		int n,q;
		double e[105],s[105],adj[105][105];
		scanf("%d%d",&n,&q);
		for(int i=0;i<n;i++) scanf("%lf%lf",&e[i],&s[i]);
		for(int i=0;i<n;i++) for(int j=0;j<n;j++) scanf("%lf",&adj[i][j]);
		for(int i=0;i<q;i++){
			int a,b;
			scanf("%d%d",&a,&b);
		}
		double dp[105];
		for(int i=0;i<n;i++) dp[i]=-1;
		dp[0]=0;
		for(int i=0;i<n-1;i++){
			double cur=0;
			for(int j=i;j<n-1;j++){
				cur+=adj[j][j+1];
				//printf("%lf ",cur);
				if(cur>e[i]) break;
				if(dp[j+1]==-1) dp[j+1]=dp[i]+cur/s[i];
				else dp[j+1]=min(dp[j+1],dp[i]+cur/s[i]);
			}
			//printf("\n");
			//for(int i=0;i<n;i++) printf("%lf ",dp[i]);
			//cout<<endl;
		}
		printf("Case #%d: %lf\n",tc,dp[n-1]);
	}
}
