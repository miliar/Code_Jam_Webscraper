#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ll, int> plli;
typedef pair<double, double> pdd;
typedef pair<string, int> psi;

const int MOD = 1e9 + 7;

const ll oo = 1e15;

typedef long long ll;

int t, ac,aj;

int dp[1442][730][2],a,b,start;

int block[1442][2];
int pre[1442][2];

int calc(int idx , int remA,bool turn){
	int remB = 720-(idx-(720-remA));
	if(remB < 0)
		return 1e9;
	if(remA < 0)
		return 1e9;
	if(idx == 1440)
		return (turn != start);
	int &ret = dp[idx][remA][turn];
	if(ret != -1)
		return ret;
	ret = 1e9;
	if(block[idx][turn])
		return ret;
	if(turn){
		if(!remA)
			return ret;
		ret = min(ret,calc(idx+1,remA-1,turn));
		ret = min(ret,1+calc(idx+1,remA-1,!turn));	
	}else{
		if(!remB)
			return ret;
		ret = min(ret,calc(idx+1,remA,turn));
		ret = min(ret,1+calc(idx+1,remA,!turn));	
	}
	return ret;
}

int main() {
 	freopen("input.txt","r",stdin);
 	freopen("output.txt","w",stdout);
 	scanf("%d",&t);
 	for(int it = 1 ; it <= t ; it++){
 		scanf("%d%d",&ac,&aj);
 		memset(block,0,sizeof block);
 		memset(pre,0,sizeof pre);
 		for (int i = 0; i < ac; ++i){
 			scanf("%d%d",&a,&b);
 			block[a][1]++;
 			block[b][1]--;
 		}
 		for (int i = 0; i < aj; ++i){
 			scanf("%d%d",&a,&b);
 			block[a][0]++;
 			block[b][0]--;
 		}
 		for (int i = 0; i < 2; ++i){
 			for(int j = 1 ; j <= 1440;j++){
 				block[j][i]+=block[j-1][i];
 			}
 		}
 		int mn = 2e9;
 		for(start = 0 ; start < 2 ; start++){
 			memset(dp,-1,sizeof dp);
 			mn = min(mn,calc(0,720,start));
 		}
 		printf("Case #%d: %d\n",it, mn);
 	}
	return 0;
}
