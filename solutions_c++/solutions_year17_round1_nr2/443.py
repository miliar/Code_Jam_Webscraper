#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int N = 50;
const double eps = 1e-8;
const double inf = 1e9;

int n, p;
int a[N], b[N][N], c[N];

bool cancal() {
	for (int i = 0; i < n; i++) if (c[i] >= p) return false;
	return true;
}
int cal() {
	double ansmin = -inf, ansmax = inf;
	for (int i = 0; i < n; i++) {
		ansmin = max(ansmin, (double)b[i][c[i]] / a[i] / 1.1);
		ansmax = min(ansmax, (double)b[i][c[i]] / a[i] / 0.9);
	}
	if (ceil(ansmin - eps) > floor(ansmax + eps) || floor(ansmax + eps) < eps) {
		int q = 0;
		for (int i = 1; i < n; i++)
			if ((double)b[i][c[i]] / a[i] < (double)b[q][c[q]] / a[q])
				q = i;
		c[q]++;
		return 0;
	} else {
		//printf("%.15f %.15f\n", ansmin, ansmax);
		for (int i = 0; i < n; i++) c[i]++;
		return 1;
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		scanf("%d%d", &n, &p);
		for (int i = 0; i < n; i++) scanf("%d", &a[i]);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < p; j++) scanf("%d", &b[i][j]);
		for (int i = 0; i < n; i++) sort(b[i], b[i] + p);
		for (int i = 0; i < n; i++) c[i] = 0;
		int ans = 0;
		while (cancal()) ans += cal();
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
