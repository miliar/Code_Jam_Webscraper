#include "bits/stdc++.h"
using namespace std;
const int N = 105;
int t , tc;
int n , p;
int arr[N];
int cnt[4];
int dp[N][N][N][4];
int wh[N][N][N][4];
int solve(int one , int two , int tree , int pre){
	if(one + two + tree == 0){
		return 0;
	}
	if(wh[one][two][tree][pre] == tc){
		return dp[one][two][tree][pre];
	}
	int res = 0;
	if(one){
		res = max(res , solve(one - 1 , two , tree , (pre + p - 1) % p));
	}
	if(two){
		res = max(res , solve(one , two - 1 , tree , (pre + p - 2) % p));
	}
	if(tree){
		res = max(res , solve(one , two , tree - 1 , (pre + p - 3) % p));
	}
	res += (pre == 0);
	wh[one][two][tree][pre] = tc;
	return dp[one][two][tree][pre] = res;
}
int main(){
	scanf("%d" , &t);
	for(tc = 1 ; tc <= t ; ++tc){
		printf("Case #%d: " , tc);
		scanf("%d %d" , &n , &p);
		memset(cnt , 0 , sizeof(cnt));
		for(int i = 1 ; i <= n ; ++i){
			scanf("%d" , arr + i);
			++cnt[arr[i] % p];
		}
		int ans = cnt[0] + solve(cnt[1] , cnt[2] , cnt[3] , 0);
		printf("%d\n" , ans);
	}
}