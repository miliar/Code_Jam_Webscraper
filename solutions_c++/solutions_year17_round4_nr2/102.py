/**
 * Sergey Kopeliovich (burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define err(...) fprintf(stderr, "%.2f : ", 1. * clock() / CLOCKS_PER_SEC), fprintf(stderr, __VA_ARGS__), fflush(stderr)

void solve() {
	int n, c, m;
	scanf("%d%d%d", &n, &c, &m);	
	assert(c == 2);
	multiset<int> a[c];
	vector<vector<int>> cnt(2, vector<int>(n));
	vector<int> all(2);
	forn(i, m) {
		int pos, who;
		scanf("%d%d", &pos, &who), pos--, who--;
		a[who].insert(pos);
		cnt[who][pos]++;
		all[who]++;
	}
	int ans = 0;
	forn(t, 2)  {
		while (a[t].size() && *a[t].begin() == 0) {
			ans++;
			a[t].erase(a[t].begin());
			auto it = a[t ^ 1].lower_bound(1);
			if (it != a[t ^ 1].end())
				a[t ^ 1].erase(it);
		}
	}
	int num = ans + max(a[0].size(), a[1].size());
	int ma = 0;
	forn(i, n)
		ma = max(ma, cnt[0][i] + cnt[1][i]);
	// printf("[%d %d] [%d %d] ", cnt[0][0], cnt[0][1], cnt[1][0], cnt[1][1]);
	printf("%d %d\n", num, max(0, ma - num));
}

int main() {
	int tn;
	scanf("%d", &tn);
	forn(t, tn) {
		printf("Case #%d: ", t + 1);
		// err("Case #%d\n", t + 1);
		solve();
	}
}
