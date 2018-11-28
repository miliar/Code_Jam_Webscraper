#include <bits/stdc++.h>
using namespace std;
int k, n,t;
int dp[2005][1005];
char p[2005];

int solve(int pos){
	//if (dp[pos][rb] > -1) return dp[pos][rb];
	if (pos > n-k) {
		for (int i = pos; i < n; ++i){
			if (p[i] != '+') return n+1;
		}
		return 0;
	}
	int need_flip = p[pos] != '+';
	if (need_flip) {
		for (int i = pos; i < pos+k; ++i){
			if (p[i]=='+'){
				p[i] = '-';
			} else {
				p[i] = '+';
			}
		}
	}
	return need_flip + solve(pos+1);
}

int main (){
	scanf("%d",&t);
	for (int tc = 1; tc <= t; ++tc){
		scanf("%s %d", p, &k);
		n = strlen(p);
		memset(dp,-1,sizeof(dp));
		int ans = solve(0);
		printf("Case #%d: ", tc);
		if (ans > n) {
			puts("IMPOSSIBLE");
		} else {
			cout << ans << endl;
		}
	}
}