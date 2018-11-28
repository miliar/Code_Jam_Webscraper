#include <bits/stdc++.h>
using namespace std;
const int N = 105;
int main() {
	int T, zzz = 0;
	scanf("%d", &T);
	while (T --) {
		int hd, ad, hk, ak, b, d;
		scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
		int ans = -1;
		for (int b_cnt = 0; b_cnt <= 100; ++ b_cnt) {
			for (int d_cnt = 0; d_cnt <= 100; ++ d_cnt) {
				//if (b_cnt + d_cnt && hd <= max(0, ak - (!!d_cnt) * d)) continue;
				int h = hd, a = ak, c = 0;
				for (int i = 0; i < d_cnt; ++ i) {
					if (h <= max(0, a - d)) {
						h = hd - a;
						i --;
					}
					else {
						a = max(0, a - d);
						h -= a;
					}
					c ++;
					if (c > 1000) break;
				}
				if (c > 1000) continue;
				int aa = ad;
				for (int i = 0; i < b_cnt; ++ i) {
					if (h <= a) {
						h = hd - a;
						i --;
					}
					else {
						aa += b;
						h -= a;
					}
					c ++;
					if (c > 1000) break;
				}
				if (c > 1000) continue;
				int hh = hk;
				//printf("bc = %d dc= %d   c=%d h=%d a=%d aa=%d\n", b_cnt, d_cnt, c, h, a, aa);
				while (hh > 0) {
					if (h <= a && hh > aa) h = hd - a; else {
						hh -= aa;
						h -= a;
					}
					c ++;
					if (c > 1000) break;
				}
				if (c > 1000) continue;
				if (ans == -1 || ans > c) ans = c;
			}
		}
		printf("Case #%d: ", ++ zzz);
		if (ans == -1) puts("IMPOSSIBLE"); else printf("%d\n", ans);
	}
}

