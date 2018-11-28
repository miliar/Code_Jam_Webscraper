#include<cstdio>
#include<utility>
#include<vector>
#include<algorithm>

int t, n, c, m, wtf[1003][1003], sp[1003];

int max(int x, int y) {
	return x > y ? x : y;
}

bool trytry(int x) {
	int y = 0;
	for (int i = n; i; i--) {
		if (y + sp[i] > x) y = y + sp[i] - x;
		else y = 0;
	}
	return y == 0;
}

int search(int l, int r) {
	int mid = (l + r) / 2;
	if (l == r) return mid;
	if (trytry(mid)) return search(l, mid);
	else return search(mid + 1, r);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	for (int test = 1; test <= t; test++) {
		scanf("%d %d %d", &n, &c, &m);
		for (int i = 1; i <= n; i++) for (int j = 1; j <= c; j++) wtf[i][j] = 0;
		for (int i = 0; i < m; i++) {
			int p, b;
			scanf("%d %d", &p, &b);
			wtf[p][b]++;
		}
		int max_b = 0;
		for (int i = 1; i <= c; i++) {
			int s = 0;
			for (int j = 1; j <= n; j++) s += wtf[j][i];
			max_b = max(max_b, s);
		}
		for (int i = 1; i <= n; i++) {
			sp[i] = 0;
			for (int j = 1; j <= c; j++) sp[i] += wtf[i][j];
		}
		int ans1 = max(max_b, search(1, 1000));
		int ans2 = 0;
		int y = 0;
		for (int i = n; i; i--) {
			if (sp[i] > ans1) ans2 += sp[i] - ans1;
			if (y + sp[i] > ans1) y = y + sp[i] - ans1;
			else y = 0;
		}
		printf("Case #%d: %d %d\n", test, ans1, ans2);
	}
}
