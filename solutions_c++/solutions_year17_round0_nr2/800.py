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
ll dp[20][10][2];
string str;

void solve(int ca){
	cin >> str;
	int n=str.size();
	memset(dp,-1,sizeof(dp));
	dp[0][0][0]=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<=9;j++){
			for(int k=j;k<=9;k++){
				if(dp[i][j][1]!=-1)dp[i+1][k][1]=max(dp[i][j][1]*10LL+k,dp[i+1][k][1]);
				if((str[i]-'0')==k){
					if(dp[i][j][0]!=-1)dp[i+1][k][0]=max(dp[i][j][0]*10LL+k,dp[i+1][k][0]);
				}else if(str[i]-'0'>k){
					if(dp[i][j][0]!=-1)dp[i+1][k][1]=max(dp[i][j][0]*10LL+k,dp[i+1][k][1]);
				}
			}
		}
	}
	ll res=0;
	for(int i=0;i<10;i++){
		res=max(res,dp[n][i][0]);
		res=max(res,dp[n][i][1]);
	}
	printf("Case #%d: %lld\n",ca,res);
}

int main(void){
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		solve(i+1);
	}
	return 0;
}
