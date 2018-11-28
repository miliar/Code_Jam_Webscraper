#include <bits/stdc++.h>
using namespace std;
typedef long long lint;
typedef pair<int, int> pi;
const int mod = 1e9 + 7;

int dp[105][105][105][105][4];
bool vis[105][105][105][105][4];

int f(int a, int b, int c, int d, int e){
	if(a + b + c + d == 0) return 0;
	if(vis[a][b][c][d][e]) return dp[a][b][c][d][e];
	int ret = 0;
	if(a > 0) ret = max(ret, f(a-1, b, c, d, e));
	if(b > 0) ret = max(ret, f(a, b-1, c, d, (e+1)%4));
	if(c > 0) ret = max(ret, f(a, b, c-1, d, (e+2)%4));
	if(d > 0) ret = max(ret, f(a, b, c, d-1, (e+3)%4));
	ret += (e == 0);
	vis[a][b][c][d][e] = 1;
	return dp[a][b][c][d][e] = ret;
}

int g(int a, int b, int c, int e){
	if(a + b + c == 0) return 0;
	if(vis[a][b][c][0][e]) return dp[a][b][c][0][e];
	int ret = 0;
	if(a > 0) ret = max(ret, g(a-1, b, c, e));
	if(b > 0) ret = max(ret, g(a, b-1, c, (e+1)%3));
	if(c > 0) ret = max(ret, g(a, b, c-1, (e+2)%3));
	ret += (e == 0);
	vis[a][b][c][0][e] = 1;
	return dp[a][b][c][0][e] = ret;
}

int h(int a, int b, int e){
	if(a + b == 0) return 0;
	if(vis[a][b][0][0][e]) return dp[a][b][0][0][e];
	int ret = 0;
	if(a > 0) ret = max(ret, h(a-1, b, e));
	if(b > 0) ret = max(ret, h(a, b-1, (e+1)%2));
	ret += (e == 0);
	vis[a][b][0][0][e] = 1;
	return dp[a][b][0][0][e] = ret;
}

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		int n, gg;
		scanf("%d %d",&n,&gg);
		memset(vis, 0, sizeof(vis));
		int cnt[4] = {};
		for(int i=0; i<n; i++){
			int x;
			cin >> x;
			x %= gg;
			cnt[x]++;
		}
		int ans = 0;
		if(gg == 2) ans = h(cnt[0], cnt[1], 0);
		if(gg == 3) ans = g(cnt[0], cnt[1], cnt[2], 0);
		if(gg == 4) ans = f(cnt[0], cnt[1], cnt[2], cnt[3], 0);
		printf("Case #%d: %d\n", i, ans);
		fflush(stdout);
	}
}
