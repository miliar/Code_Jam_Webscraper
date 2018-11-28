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

int t;
int hd,ad,hk,ak,b,d;
int dp[101][101][101];
int tmp[101][101][101];
void solve(int ta){
	memset(dp,-1,sizeof(dp));
	dp[hd][hk][ak]=ad;
	bool flag=true;
	int v=0;
	int res=11451419;
	while(flag){
		flag=false;
		v++;
		memset(tmp,-1,sizeof(tmp));
		for(int i=0;i<=100;i++){
			for(int j=0;j<=100;j++){
				for(int k=0;k<=100;k++){
					if(dp[i][j][k]>0){
						//printf("%d %d %d %d %d\n",v,i,j,k,dp[i][j][k]);
						if(j-dp[i][j][k]<=0){
							printf("Case #%d: %d\n",ta,min(v,res));
							return;
						}
						if(k==0){
							int at=j/dp[i][j][k];
							if(j%dp[i][j][k]!=0)at++;
							res=min(res,v-1+at);
							tmp[i][j][k]=max(tmp[i][j][k],dp[i][j][k]+b);
							flag=true;
						}else{
							if(i-k>0){
								tmp[i-k][j-dp[i][j][k]][k]=max(tmp[i-k][j-dp[i][j][k]][k],dp[i][j][k]);
								tmp[i-k][j][k]=max(tmp[i-k][j][k],dp[i][j][k]+b);
								flag=true;
							}
							int nd=max(0,k-d);
							if(i-nd>0){
								tmp[i-nd][j][nd]=max(tmp[i-nd][j][nd],dp[i][j][k]);
								flag=true;
							}
							if(hd-k>i){
								tmp[hd-k][j][k]=max(tmp[hd-k][j][k],dp[i][j][k]);
								flag=true;
							}
						}
					}
				}
			}
		}
		for(int i=0;i<=100;i++){
			for(int j=0;j<=100;j++){
				for(int k=0;k<=100;k++){
					dp[i][j][k]=tmp[i][j][k];
				}
			}
		}
	}
	if(res==11451419)printf("Case #%d: IMPOSSIBLE\n",ta);
	else printf("Case #%d: %d\n",ta,res);
}

int main(void){
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%d%d%d%d%d%d",&hd,&ad,&hk,&ak,&b,&d);
		solve(i+1);
	}
	return 0;
}
