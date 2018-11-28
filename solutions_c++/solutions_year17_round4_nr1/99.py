#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<deque>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<stdlib.h>
#include<cassert>
using namespace std;
const long long mod=1000000007;
const long long inf=mod*mod;
const long long d2=500000004;
const double EPS=1e-10;
const double PI=acos(-1.0);
int ABS(int a){return max(a,-a);}
long long ABS(long long a){return max(a,-a);}
int a[110];
int sz[11];
int dp[110][110][110];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int N,P;
		scanf("%d%d",&N,&P);
		for(int i=0;i<N;i++)scanf("%d",a+i);
		for(int i=0;i<11;i++)sz[i]=0;
		for(int i=0;i<N;i++){
			sz[a[i]%P]++;
		}
		for(int i=0;i<110;i++)for(int j=0;j<110;j++)for(int k=0;k<110;k++)dp[i][j][k]=-mod;
		dp[0][0][0]=sz[0];

		for(int i=0;i<=sz[1];i++){
			for(int j=0;j<=sz[2];j++){
				for(int k=0;k<=sz[3];k++){
					if(dp[i][j][k]<0)continue;
					int tot=(1*i+2*j+3*k)%P;
					if(i<sz[1])dp[i+1][j][k]=max(dp[i+1][j][k],dp[i][j][k]+(tot==0));
					if(j<sz[2])dp[i][j+1][k]=max(dp[i][j+1][k],dp[i][j][k]+(tot==0));
					if(k<sz[3])dp[i][j][k+1]=max(dp[i][j][k+1],dp[i][j][k]+(tot==0));

				}
			}
		}
		printf("Case #%d: %d\n",t,dp[sz[1]][sz[2]][sz[3]]);
	}
}