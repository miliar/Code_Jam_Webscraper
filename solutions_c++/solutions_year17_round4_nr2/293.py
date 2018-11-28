#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int nmax = 1000 + 18, mmax = 1000 + 18;

int v[nmax], w[mmax];
int ans_l, ans_r;
int n, c, m, T;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		scanf("%d%d%d", &n, &c, &m);
		memset(v, 0, sizeof(v));
		memset(w, 0, sizeof(w));
		for (int i = 1; i <= m; ++i) {
			int p, b;
			scanf("%d%d", &p, &b);
			++v[p];
			++w[b];
		}
		int maxcus = 0, maxpos = 0;
		for (int i = 1; i <= n; ++i)
			if (v[i] > maxpos)
				maxpos = v[i];
		for (int i = 1; i <= c; ++i)
			if (w[i] > maxcus)
				maxcus = w[i];
		if (maxcus >= maxpos)
			printf("Case #%d: %d %d\n", cases, maxcus, 0);
		else {
			int ans = 0, s = 0;
			for (int i = 1; i <= n; ++i) {
				s += v[i];
				int ave = s / i;
				if (ave * i < s) ++ave;
				if (ave > ans)
					ans = ave;
			}
			if (ans < maxcus)
				ans = maxcus;
			int ans2 = 0;
			for (int i = 1; i <= n; ++i) {
				if (v[i] > ans) {
					ans2 += v[i] - ans;
				}
			}
			printf("Case #%d: %d %d\n", cases, ans, ans2);
		}
	}
	return 0;
}
