#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <functional>
#include <iostream>
#define MOD 1000000007LL
using namespace std;
typedef long long ll;
typedef pair<int,int> P;

int t,n,p;
int g[101];
int dp[2][101][101][101];

int solve(){
	memset(dp,-1,sizeof(dp));
	dp[0][0][0][0]=0;
	int now=1,prev=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<=i;j++){
			for(int k=0;k<=i-j;k++){
				for(int l=0;l<=i-j-k;l++){
					if(dp[prev][j][k][l]==-1)continue;
					if(g[i]%p==0){
						dp[now][j][k][l]=max(dp[now][j][k][l],dp[prev][j][k][l]+1);
					}
					if(g[i]%p==1){
						if(p==2){
							dp[now][j+1][k][l]=max(dp[now][j+1][k][l],dp[prev][j][k][l]+1);
							if(j>=1)dp[now][j-1][k][l]=max(dp[now][j-1][k][l],dp[prev][j][k][l]);
						}
						if(p==3){
							dp[now][j][k+1][l]=max(dp[now][j][k+1][l],dp[prev][j][k][l]+1);
							if(j>=1)dp[now][j-1][k][l]=max(dp[now][j-1][k][l],dp[prev][j][k][l]);
							if(k>=1)dp[now][j+1][k-1][l]=max(dp[now][j+1][k-1][l],dp[prev][j][k][l]);
						}
						if(p==4){
							dp[now][j][k][l+1]=max(dp[now][j][k][l+1],dp[prev][j][k][l]+1);
							if(j>=1)dp[now][j-1][k][l]=max(dp[now][j-1][k][l],dp[prev][j][k][l]);
							if(k>=1)dp[now][j+1][k-1][l]=max(dp[now][j+1][k-1][l],dp[prev][j][k][l]);
							if(l>=1)dp[now][j][k+1][l-1]=max(dp[now][j][k+1][l-1],dp[prev][j][k][l]);
						}
					}
					if(g[i]%p==2){
						if(p==3){
							dp[now][j+1][k][l]=max(dp[now][j+1][k][l],dp[prev][j][k][l]+1);
							if(k>=1)dp[now][j][k-1][l]=max(dp[now][j][k-1][l],dp[prev][j][k][l]);
							if(j>=1)dp[now][j-1][k+1][l]=max(dp[now][j-1][k+1][l],dp[prev][j][k][l]);
						}
						if(p==4){
							dp[now][j][k+1][l]=max(dp[now][j][k+1][l],dp[prev][j][k][l]+1);
							if(k>=1)dp[now][j][k-1][l]=max(dp[now][j][k-1][l],dp[prev][j][k][l]);
							if(j>=1)dp[now][j-1][k][l+1]=max(dp[now][j-1][k][l+1],dp[prev][j][k][l]);
							if(l>=1)dp[now][j+1][k][l-1]=max(dp[now][j+1][k][l-1],dp[prev][j][k][l]);
						}
					}
					if(g[i]%p==3){
						if(p==4){
							dp[now][j][k][l+1]=max(dp[now][j][k][l+1],dp[prev][j][k][l]+1);
							if(l>=1)dp[now][j][k][l-1]=max(dp[now][j][k][l-1],dp[prev][j][k][l]);
							if(k>=1)dp[now][j][k-1][l+1]=max(dp[now][j][k-1][l+1],dp[prev][j][k][l]);
							if(j>=1)dp[now][j-1][k+1][l]=max(dp[now][j-1][k+1][l],dp[prev][j][k][l]);
						}
					}
				}
			}
		}
		swap(now,prev);
		memset(dp[now],-1,sizeof(dp[now]));
	}
	int maxi=dp[prev][0][0][0];
	maxi=max(dp[prev][1][0][0],maxi);
	maxi=max(dp[prev][0][1][0],maxi);
	maxi=max(dp[prev][0][0][1],maxi);
	return maxi;
}

int main(void){
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%d%d",&n,&p);
		for(int j=0;j<n;j++){
			scanf("%d",&g[j]);
		}
		printf("Case #%d: %d\n",i+1,solve());
	}
	return 0;
}
