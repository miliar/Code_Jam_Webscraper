#include <bits/stdc++.h>
using namespace std;

int h[110], g[110];
int hd,ad,hk,ak,b,d;
int T, t_;

int solve(int step, int nowu, int nowv, int au, int av) {
	int ans = 0;
	while (step && ans <= 500) {
		ans++;
		if (nowu <= av) { nowu = hd; }
		else {
			au += b;
			step--;
		}
		nowu -= av;
		if (nowu <= 0) return 510;
	}
	while (ans <= 500 && nowv > 0) {
		ans++;
		if (nowu <= av && nowv > au) {
			nowu = hd;
		} else {
			nowv -= au;
		}
		nowu -= av;
		if (nowv > 0 && nowu <= 0) return 510;
	}
	return ans;
}

int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	for (scanf("%d",&T); T; T--) {
		scanf("%d %d %d %d %d %d",&hd,&ad,&hk,&ak,&b,&d);
		h[0] = hd;
		g[0] = 0;
		printf("Case #%d: ",++t_);
		for (int i = 1; i <= 100; i++) {
			h[i] = h[i - 1];
			g[i] = g[i - 1];
			if (h[i] <= 0) continue;
			if (h[i] <= max(0, ak - d * i)) {
				h[i] = hd - max(0, ak - d * (i - 1));
				g[i]++;
			}
			h[i] -= max(0, ak - d * i);
		}
		int ans = 1 << 30;
		for (int j = 0; j <= 100; j++) {
			if (h[j] <= 0) continue;
			int av = max(ak - d * j, 0);	
			int sing = j + g[j];
			int nowu = h[j];
			int nowv = hk;
			for (int i = 0; i <= 100; i++)				
				ans = min(ans, sing + solve(i, nowu, nowv, ad, av));
		}
		if (ans <= 490) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
