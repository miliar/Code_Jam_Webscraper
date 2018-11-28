#include "bits/stdc++.h"
using namespace std;
const int N = 105;
const int inf = 1e8 + 8;
int t;
int hd , ad;
int hk , ak;
int b , d;
int now(int heal , int ad , int ak){
	int res = 0;
	int h = hk;
	while(h > 0){
		if(ad >= h){
			++res;
			h = 0;
			break;
		}
		if(ak >= heal){
			heal = hd - ak;
			++res;
			if(ak >= heal){
				res = inf;
				break;
			}
		}
		h -= ad;
		heal -= ak;
		++res;
	}
	return res;
}
int dp[N][N][N];
int solve(int heal , int buffs , int debuffs){
	if(heal <= 0){
		return inf;
	}
	if(dp[heal][buffs][debuffs] != -1){
		return dp[heal][buffs][debuffs];
	}
	int res = inf;
	if(d > 0){
		if((d * debuffs < ak) && (heal > max(0 , (ak - (debuffs + 1) * d)))){
			res = min(res , 1 + solve(heal - max(0 , (ak - (debuffs + 1) * d)) , buffs , debuffs + 1));
		}
	}
	if(b > 0){
		if(ad + b * buffs < hk && heal > max(0 , (ak - debuffs * d))){
			res = min(res , 1 + solve(heal - max(0 , (ak - debuffs * d)) , buffs + 1 , debuffs));
		}
	}
	if(heal < hd - max(0 , (ak - debuffs * d))){
		res = min(res , 1 + solve(hd - max(0 , (ak - debuffs * d)) , buffs , debuffs));
	}
	res = min(res , now(heal , ad + b * buffs , ak - d * debuffs));
	return dp[heal][buffs][debuffs] = res;
}
int main(){
	scanf("%d" , &t);
	for(int tc = 1 ; tc <= t ; ++tc){
		printf("Case #%d: " , tc);
		scanf("%d %d %d %d %d %d" , &hd , &ad , &hk , &ak , &b , &d);
		memset(dp , -1 , sizeof(dp));
		int ans = solve(hd , 0 , 0);
		if(ans >= inf){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("%d\n" , ans);
		}
	}
}