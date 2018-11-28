#include <bits/stdc++.h>

using namespace std;

int a[200001];
int n, p;
int tp = 0;

int main( ) {
	int T;
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	while (T --) {
		int cnt = 0;
		scanf("%d", &n);
		scanf("%d", &p);
		for (int i = 1; i <= n; i ++)
			scanf("%d", &a[i]);
		printf("Case #%d: ", ++ tp);
		if (p == 2) {
			for (int i = 1; i <= n; i ++)
				if (a[i] % 2 == 0) ++ cnt;
			printf("%d\n", cnt + (n - cnt + 1) / 2);
		}
		else if (p == 3) {
			int aa = 0, b = 0;
			for (int i = 1; i <= n; i ++)
				if (a[i] % 3 == 0) ++ cnt;
				else if (a[i] % 3 == 1) ++ aa;
				else ++ b;
			int ans = 0;
			ans += cnt;
			int tmp = min(aa, b);
			ans += tmp;
			aa -= tmp, b -= tmp;
			if (aa) ans += (aa + 2) / 3;
			else ans += (b + 2) / 3;
			printf("%d\n", ans);
		}
		else {
			int aa = 0, bb = 0, cc = 0, dd = 0;
			for (int i = 1; i <= n; i ++)
				if (a[i] % 4 == 0) ++ aa;
				else if (a[i] % 4 == 1) ++ bb;
				else if (a[i] % 4 == 2) ++ cc;
				else ++ dd;
			int ans = 0;
			ans += aa;
			ans += cc / 2;
			cc %= 2;
			int tmp = min(bb, dd);
			ans += tmp;
			bb -= tmp, dd -= tmp;
			
			if (cc == 0) {
				if (bb) ans += (bb + 3) / 4;
				else ans += (dd + 3) / 4;
			}
			else {
				if (bb) {
					if (bb <= 2) ans ++;
					else ans += 1 + (bb - 2 + 3) / 4;
				}
				else {
					if (dd <= 2) ans ++;
					else ans += 1 + (dd - 2 + 3) / 4;
				}
			}
			printf("%d\n", ans);
		}
	}
	return 0;
}
