// Problem B. Ratatouille
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int n, p;
int r[64];
int q[64][64];
int ans;

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		scanf("%d %d", &n, &p);
		for (int i = 0; i < n; i++) scanf("%d", &r[i]);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < p; j++) scanf("%d", &q[i][j]);
			sort(q[i], q[i] + p);
		}

		ans = 0;
		if (n == 1) {
			for (int j = 0; j < p; j++) {
				int t = r[0] * (q[0][j] / r[0]);
				if (abs(t + r[0] - q[0][j]) < abs(t - q[0][j])) t += r[0];
				int d = abs(q[0][j] - t);
				if (d * 10 <= t) ans++;
			}
		} else if (n == 2) {
			do {
				int x = 0;
				for (int j = 0; j < p; j++) {
					for (int m = min(q[0][j] / r[0], q[1][j] / r[1]); ; m++) {
						int t0 = r[0] * m, t1 = r[1] * m;
						int d0 = abs(q[0][j] - t0), d1 = abs(q[1][j] - t1);
						if (d0 * 10 <= t0 && d1 * 10 <= t1) {
							x++;
							break;
						}
						if (t0 > q[0][j] && t1 > q[1][j]) break;
					}
				}
				if (x > ans) ans = x;
			} while (next_permutation(q[0], q[0] + p));
		}

		printf("Case #%d: %d\n", ti, ans);
	}

	return 0;
}
