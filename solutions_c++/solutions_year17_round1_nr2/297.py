#include <bits/stdc++.h>

using namespace std;

int a[1001];
int b[1001][1001];
pair<pair<int, int>, int> stk[100001];
int n, m;
int c[10001];

priority_queue<int > q[1001];

const double eps = 1e-8;

int dcmp(double x) { return fabs(x) <= eps ? 0 : (x > 0 ? 1 : -1); }
int main( ) {
	int T, tp = 0;
	scanf("%d", &T);
	while (T --) {
		int top = 0;
		scanf("%d %d", &n, &m);
		for (int i = 1; i <= n; i ++)
			scanf("%d", &a[i]);
		for (int i = 1; i <= n; i ++)
			for (int j = 1; j <= m; j ++)
				scanf("%d", &b[i][j]);
		for (int i = 1; i <= n; i ++) {
			for (int j = 1; j <= m; j ++) {
				double tmp = b[i][j] * 1. / (0.9 * a[i]);
				int x = floor(tmp + eps);
				if (x == 0) continue;
				if (dcmp(b[i][j] - a[i] * x * 1.1) > 0) continue;
				tmp = b[i][j] * 1. / (1.1 * a[i]);
				int y = ceil(tmp - eps);
				if (dcmp(b[i][j] - a[i] * y * 0.9) < 0) continue;
				if (y == 0) ++ y;
				stk[++ top] = make_pair(make_pair(y, x), i);
					
			}
		}
		int ans = 0;
		for (int i = 1; i <= n; i ++)
			while (!q[i].empty()) q[i].pop();
		sort(stk + 1, stk + 1 + top);
		for (int i = 1; i <= top; i ++) {
			int tmp = i;
			while (tmp <= top && stk[tmp].first.first == stk[i].first.first) ++ tmp;
			-- tmp;
			for (int j = i; j <= tmp; j ++) {
				int id = stk[j].second;
				q[id].push(-stk[j].first.second);
			}
			int mx = 0x3f3f3f3f;
			for (int j = 1; j <= n; j ++) {
				while (!q[j].empty() && -q[j].top() < stk[i].first.first) q[j].pop();
				mx = min(mx, (int )q[j].size());
			}
			if (mx) {
				ans += mx;
				for (int j = 1; j <= n; j ++) {
					for (int k = 1; k <= mx; k ++) q[j].pop();
				}
			}
			i = tmp;
		}
		printf("Case #%d: %d\n", ++ tp, ans);
	}
	return 0;
}
