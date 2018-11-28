#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
LL n;
int dig, T;
int d[110];
LL ans;
void dfs(int p, int nowd, LL prefix, int o){
	if (p == dig){
		if (prefix <= n && prefix > ans) ans = prefix;
		return;
	}
	if (!o){
		if (nowd > d[p]) return;
		dfs(p + 1, d[p], prefix * 10 + d[p], o);
		for (int i = nowd; i < d[p]; i++)
			dfs(p + 1, i, prefix * 10 + i, 1);
	}else {
		for (int i = nowd; i < 10; i++)
			dfs(p + 1, i, prefix * 10 + i, 1);
	}
}
int main(){
	//		freopen("a.txt", "r", stdin);
	//		freopen("ans.txt", "w", stdout);
	scanf("%d\n", &T);
	for (int tt = 1; tt <= T; tt++){
		printf("Case #%d: ", tt);
		scanf("%lld\n", &n);
		LL x = n;
		dig = 0;
		while (x != 0) x /= 10, dig++;
		x = n;
		for (int i = dig - 1; i >= 0; i--)
			d[i] = x % 10, x /= 10;
		ans = -1;
		dfs(0, 1, 0, 0);
		if (ans == -1){
			dig --;
			ans = 0;
			for (int i = 1; i <= dig; i++)
				ans = ans * 10 + 9;
		}
		printf("%lld\n", ans);
	}
	return 0;
}
