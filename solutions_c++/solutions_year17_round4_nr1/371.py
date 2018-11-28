#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int n,P;
int dp[2][400][400][4];
int num[4];
void update(int &k1,int k2){
	k1=min(k1,k2);
}
int solve(){
	scanf("%d%d",&n,&P);
	memset(num,0x00,sizeof num);
	for (int i=1;i<=n;i++){
		int k1; scanf("%d",&k1); num[k1%P]++;
	}
	memset(dp,0x3f,sizeof dp);
	int now=0; dp[0][0][0][0]=0;
	int rem=num[1]+num[2]+num[3];
	for (int t=0;t<rem;t++){
		int ne=now^1;
		memset(dp[ne],0x3f,sizeof dp[ne]);
		for (int i=0;i<=num[1];i++)
			for (int j=0;j<=num[2];j++)
				for (int k=0;k<P;k++)
					if (dp[now][i][j][k]<1e8){
						int w=dp[now][i][j][k];
						if (k) w++;
						int c=t-i-j;
						if (i<num[1]) update(dp[ne][i+1][j][(k+1)%P],w);
						if (j<num[2]) update(dp[ne][i][j+1][(k+2)%P],w);
						if (c<num[3]) update(dp[ne][i][j][(k+3)%P],w);
					}
		now=ne;
	}
	int ans=1e9;
	for (int i=0;i<=num[1];i++)
		for (int j=0;j<=num[2];j++)
			for (int k=0;k<P;k++)
				ans=min(ans,dp[now][num[1]][num[2]][k]);
	return rem-ans+num[0];
}
int main(){
	freopen("Al.in","r",stdin);
	freopen("Al.out","w",stdout);
	int t; scanf("%d",&t);
	for (int i=1;i<=t;i++)
		printf("Case #%d: %d\n",i,solve());
	return 0;
}

