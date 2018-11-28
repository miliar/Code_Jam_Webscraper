#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1e5 + 5;

int n, m, c, co[MAXN], nm[MAXN], s[MAXN];

bool chk(int num) {
	int left = num * n;
	for (int i = n; i; i --) {
		left = min(left - co[i], num * (i - 1));
		if (left < 0) return 0;
	}
	return 1;
}

void solve(int tim) {
	memset(co, 0, sizeof co);
	memset(nm, 0, sizeof nm);
	printf("Case #%d: ", tim);
	scanf("%d%d%d", &n, &c, &m);
	for (int i = 1; i <= m; i ++) {
		int p;
		scanf("%d%d", &s[i], &p);
		co[s[i]] ++;
		nm[p] ++;
	}
	int cnt = 0, lim = 0;
	for (int i = 1; i <= c; i ++) lim = max(lim, nm[i]);
	int l = lim, r = m, ans = 0;
	while (l <= r) {
		int mid = (l + r) >> 1;
		if (chk(mid)) r = mid - 1, ans = mid; else
			l = mid + 1;
	}
	int sum = 0;
	for (int i = 1; i <= n; i ++) sum += max(0, co[i] - ans);
	printf("%d %d\n", ans, sum);
}

int main() {
	//freopen("data.in", "r", stdin), freopen("data.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++) solve(i);
}