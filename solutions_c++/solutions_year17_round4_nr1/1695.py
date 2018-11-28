#include<iostream>
#include<cstdio>
#include<algorithm>
#include<math.h>
#include<vector>
#include<map>
#include<string.h>
#include<queue>
#include<limits.h>
#include<stdlib.h>
#pragma warning(disable : 4996)
using namespace std;

signed main() {
	freopen("X.txt", "w", stdout);
	int a; cin >> a;
	for (int b = 1; b <= a; b++) {
		int c[4]{};
		int d, e; cin >> d >> e;
		for (int f = 0; f < d; f++) {
			int g; cin >> g;
			c[g%e]++;
		}
		int ans = 0;
		if (e == 2) {
			ans = c[0] + (c[1] - c[1] / 2);
		}
		else if (e == 3) {
			ans = c[0];
			int h = min(c[1], c[2]);
			c[1] -= h; c[2] -= h;
			ans += h;
			int i = max(c[1], c[2]);
			ans += i / 3;
			if (i % 3)ans++;
		}
		else if (e == 4) {

		}
		printf("Case #%d: %d\n", b, ans);
	}
}