#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int tcn, tc, t, chk[202][10], asd;
ll n, p[202][10], dp[202][10], ret;

void ini(){
	for(int i = 1; i <= 9; i++) p[1][i] = i;
	for(int i = 2; i <= 200; i++){
		for(int j = 1; j <= 9; j++){
			p[i][j] = p[i - 1][j] + p[i][j - 1];
		}
	}
}

int g(int x, int y){
	if(x > t) return 1;
	if(chk[x][y] == asd) return dp[x][y];
	dp[x][y] = 0;
	for(int i = y; i <= 9; i++) dp[x][y] += g(x + 1, i);
	chk[x][y] = asd;
	return dp[x][y];
}

void f(int x, int y, int k){
	if(x > t) return;
	for(int i = y; i <= 9; i++){
		if(i == 9 || g(x + 1, i) >= k){
			ret *= 10;
			ret += i;
			f(x + 1, i, k);
			return;
		}
		k -= g(x + 1, i);
    }
}

ll h(int n){
	asd++;
	for(int i = 1; i <= 200; i++){
		if(p[i][9] >= n){t = i; ret = 0; f(1, 1, n); break; }
		n -= p[i][9];
	}
	return ret;
}

int main(){
	freopen("Bl.in", "r", stdin);
	freopen("Bl.out", "w", stdout);
	ini();
	scanf("%d", &tcn); for(tc = 1; tc <= tcn; tc++){
		scanf("%lld", &n);
		printf("Case #%d: ", tc);
		int s = 1, e = 5000000;
		while(s <= e){
			int m = (s + e) / 2;
			if(h(m) > n) e = m - 1;
			else s = m + 1;
		}
		printf("%lld\n", h(e));
	}
}
