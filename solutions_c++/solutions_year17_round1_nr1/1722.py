#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <list>


using namespace std;

#define N 26

char ss[N][N];
int n, m;

void solve(int lx, int ly, int rx, int ry, int sta) {
	if (sta == (sta & (-sta))) {
		char ch;
		for (int i = 0; i < N; i++) {
			if (sta & (1 << i)) {
				ch = i + 'A';
			}
		}

		for (int i = lx; i <= rx; i++) {
			for (int j = ly; j <= ry; j++) {
				ss[i][j] = ch;
			}
		}
		return;
	}
	int sum[N];
	memset(sum, 0, sizeof(sum));

	for (int i = lx; i <= rx; i++) {
		sum[i] = 0;
		for (int j = ly; j <= ry; j++) {
			if (ss[i][j] == '?') continue;
			sum[i] |= 1 << (ss[i][j] - 'A');
		}
	}

	//cout << sum[0] << ' ' << sum[1] << ' ' << sum[2] << endl;

	for (int i = lx; i <= rx - 1; i++) {
		int sa = 0, sb = 0;
		for (int j = lx; j <= i; j++) {
			sa |= sum[j];
		}

		for (int j = i + 1; j <= rx; j++) {
			sb |= sum[j];
		}
		if (sa & sb) continue;
		if (!sa || !sb) continue;

		solve(lx, ly, i, ry, sa);
		solve(i + 1, ly, rx, ry, sb);
		return;
	}

	memset(sum, 0, sizeof(sum));

	for (int i = ly; i <= ry; i++) {
		sum[i] = 0;
		for (int j = lx; j <= rx; j++) {
			if (ss[j][i] == '?') continue;
			sum[i] |= 1 << (ss[j][i] - 'A');
		}
	}

	for (int i = ly; i <= ry - 1; i++) {
		int sa = 0, sb = 0;
		for (int j = ly; j <= i; j++) {
			sa |= sum[j];
		}

		for (int j = i + 1; j <= ry; j++) {
			sb |= sum[j];
		}
		if (sa & sb) continue;
		if (!sa || !sb) continue;

		solve(lx, ly, rx, i, sa);
		solve(lx, i + 1, rx, ry, sb);
		return;
	}
}

int main() {
	int test;
	scanf("%d", &test);
	for (int cas = 1; cas <= test; cas++) {
		scanf("%d%d", &n, &m);
		int sta = 0;
		for (int i = 0; i < n; i++) {
			scanf("%s", ss[i]);
			for (int j = 0; j < m; j++) {
				if (ss[i][j] == '?') continue;
				sta |= (1 << (ss[i][j] - 'A'));
			}
		}
		solve(0, 0, n - 1, m - 1, sta);
		printf("Case #%d:\n", cas);
		for (int i = 0; i < n; i++) {
			puts(ss[i]);
		}
	}
	return 0;
}
