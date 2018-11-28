//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define inf 10000000000000
typedef long long int LL;
struct P{
	int e,s;
}c[102];
LL mp[102][102];
double dp[102][102];
double best[102];
int main(void){
    int t;
    scanf("%d",&t);
    for(int hh=1;hh<=t;hh++){
		int n,q;
		scanf("%d%d",&n,&q);
		int i,j,k;
		for(i=0;i<n;i++)
			scanf("%d%d",&c[i].e,&c[i].s);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++){
				scanf("%lld",&mp[i][j]);
				if(mp[i][j]==-1) mp[i][j]=inf;
			}
		for(k=0;k<n;k++)
			for(i=0;i<n;i++)
				for(j=0;j<n;j++)
					mp[i][j]=min(mp[i][j], mp[i][k]+mp[k][j]);
		printf("Case #%d: ",hh);
		for(int gg=0;gg<q;gg++){
			int st,ed;
			scanf("%d%d",&st,&ed);
			st--, ed--;
			for(i=0;i<n;i++)
				for(j=0;j<n;j++)
					dp[i][j]=(double)inf;
			for(i=0;i<n;i++)
				best[i]=(double)inf;
			dp[st][st]=0.0;
			best[st]=0;
			for(int ww=0;ww<n;ww++){
				for(j=0;j<n;j++){
					if(j==st) continue;
					for(i=0;i<n;i++){
						if(j==i) continue;
						if(mp[i][j]<=c[i].e)
							dp[j][i]=best[i]+(double)mp[i][j]/c[i].s;
						//printf("%d %d: %lf\n",j,i,dp[j][i]);
					}
					for(i=0;i<n;i++) best[j]=min(best[j], dp[j][i]);
					//printf("%d %lf\n",j,best[j]);
				}
			}
			printf("%lf ",best[ed]);
		}
		printf("\n");
	}
    return 0;
}
