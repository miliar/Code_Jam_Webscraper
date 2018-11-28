#define x first
#define y second
#include<bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
const int MAXT=24*60;
int t,n,m,a,b;
int s[MAXT+5];
int dp[2][2][MAXT+5][MAXT+5];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	REP(_,t){
		memset(s,0,sizeof(s));
		scanf("%d%d",&n,&m);
		while(n--){
			scanf("%d%d",&a,&b);
			for(int i=a+1;i<=b;++i){
				s[i]=1;
			}
		}
		while(m--){
			scanf("%d%d",&a,&b);
			for(int i=a+1;i<=b;++i){
				s[i]=-1;
			}
		}
		memset(dp,0x3f,sizeof(dp));
		for(int i=1;i<=MAXT;++i){
			for(int j=1;j<=i;++j){
				if(i==1){
					if(s[i]!=1){
						dp[1][1][i][j]=0;
					}
					if(s[i]!=-1){
						dp[0][0][i][j]=0;
					}
				}else{
					if(s[i]!=1){
						dp[1][0][i][j]=min(dp[1][0][i-1][j-1],dp[0][0][i-1][i-j]+1);
						dp[1][1][i][j]=min(dp[1][1][i-1][j-1],dp[0][1][i-1][i-j]+1);
					}
					if(s[i]!=-1){
						dp[0][0][i][j]=min(dp[0][0][i-1][j-1],dp[1][0][i-1][i-j]+1);
						dp[0][1][i][j]=min(dp[0][1][i-1][j-1],dp[1][1][i-1][i-j]+1);
					}
				}
			}
		}
		//printf("..%d %d\n",dp[0][0][MAXT][MAXT/2],dp[1][0][MAXT][MAXT/2]);
		//printf("..%d %d\n",dp[0][1][MAXT][MAXT/2],dp[1][1][MAXT][MAXT/2]);
		int ans=min({dp[0][0][MAXT][MAXT/2],dp[1][0][MAXT][MAXT/2]+1,dp[0][1][MAXT][MAXT/2]+1,dp[1][1][MAXT][MAXT/2]});
		printf("Case #%d: %d\n",_+1,ans);
	}
	return 0;
}

