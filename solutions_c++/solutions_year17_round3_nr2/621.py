#include <bits/stdc++.h>
#define MAX 100001
#define ll long long
#define M 1000000007
#define INF 1000000000
using namespace std;

int aj,ak,mp[2000],dp[2000][1000][2][2];

int DP(int i,int done,int prev,int first){
	if (done<0) return INF;
	if (dp[i][done][prev][first]) return dp[i][done][prev][first];
	if (i==1440){
		if (!done){
			if (prev==first) return 0;
			else return 1;
		}
		else return INF;
	}
	if (i==0){
		dp[i][done][prev][first] = min(DP(i+1,done-1,0,0),DP(i+1,done,1,1));
		return dp[i][done][prev][first];
	}
	if (prev==0){
		if (mp[i]==1) dp[i][done][prev][first] = DP(i+1,done-1,0,first);
		else if (mp[i]==-1) dp[i][done][prev][first] = 1+DP(i+1,done,1,first);
		else dp[i][done][prev][first] = min(DP(i+1,done-1,0,first),1+DP(i+1,done,1,first));
	}
	else{
		if (mp[i]==-1) dp[i][done][prev][first] = DP(i+1,done,1,first);
		else if (mp[i]==1) dp[i][done][prev][first] = 1+DP(i+1,done-1,0,first);
		else dp[i][done][prev][first] = min(1+DP(i+1,done-1,0,first),DP(i+1,done,1,first));
	}
	return dp[i][done][prev][first];
}

int main(){
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);
	int t,cs = 1;
	cin >> t;
	while(t--){
		cin >> aj >> ak;
		memset(mp,0,sizeof(mp));
		for (int i=0;i<aj;i++){
			int x,y;cin >> x >> y;
			for (int j=x;j<y;j++) mp[j] = -1;
		}
		for (int i=0;i<ak;i++){
			int x,y;cin >> x >> y;
			for (int j=x;j<y;j++) mp[j] = 1;
		}
		for (int i=0;i<=1440;i++){
			for (int j=0;j<=720;j++){
				for (int k=0;k<2;k++) dp[i][j][k][0] = dp[i][j][k][1] = 0;
			}
		}
		printf("Case #%d: %d\n",cs++,DP(0,720,0,0));
	}
	return 0;
}