#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

#define MAXN (50+5)
#define MAXP (50+5)

int t, n, p;
int r[MAXN];
//int q[MAXN][MAXP];
int least[MAXN][MAXP], most[MAXN][MAXP];
int pp[MAXN];
int ans;
int m;
bool flag[MAXN][MAXP];

bool solve(int k, int ll, int rr, int now) {
	//if (now + n - k <= ans) 
	//printf("%d %d\n", k, now);
	int l1, r1;
	if (k >= n) {
		ans = max(ans, now + 1);
		if (ans == m) return true;
		if (solve(0, 0, 2000000, now + 1)) return true;
	}else {
		for (int i = 0;i < pp[k];++i) 
			if (flag[k][i]) {
				l1 = max(least[k][i], ll);
				r1 = min(most[k][i], rr);
				if (l1 <= r1) {
					flag[k][i] = false;
					if (solve(k + 1, l1, r1, now)) return true;
					flag[k][i] = true;
				}
			}

	}

	return false;

}

int main() {
	int k, x;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	scanf("%d%*c", &t);
	for (int i = 1;i <= t;++i) {
		scanf("%d%d%*c", &n, &p);
		for (int ii = 0;ii < n;++ii)
			scanf("%d", &r[ii]);
		m = 0;
		for (int ii = 0;ii < n;++ii) {
			k = 0;
			for (int jj = 0;jj < p;++jj) {
				scanf("%d", &x);
				most[ii][k] = x / (0.9 * r[ii]);
				least[ii][k] = x / (1.1 * r[ii]);
				if (least[ii][k] * 1.1 * r[ii] < x) least[ii][k]++;
				//printf("%d %d %lf\n", least[ii][k], most[ii][k], x / (0.9 * r[ii]));
				flag[ii][k] = true;
				if (least[ii][k] <= most[ii][k]) k++;
				

			}
			pp[ii] = k;
			m = max(m, k);
		}
		ans = 0;
		solve(0, 1, 2000000, 0);
		printf("Case #%d: %d\n", i, ans);
	}

	return 0;
}