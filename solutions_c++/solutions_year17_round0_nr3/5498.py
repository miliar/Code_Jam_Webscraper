#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int N, K;
int a[1005];
int main() {
	int T; for (scanf("%d", &T); T--; ) {
		scanf("%d%d", &N, &K);
		memset(a, 0, sizeof(a));
		a[0] = a[N + 1] = 1;
		int s, minv, maxv;
		for (int j = 1; j <= K; j++) {
			s = 0, minv = -1, maxv = 2147483647;
			for (int i = 1; i <= N; i++) {
				if (a[i]) continue;
				int L = 0, R = 0;
				for (int k = i - 1; k >= 0; k--) if (a[k]) { L = k; break; }
				for (int k = i + 1; k <= N + 1; k++) if (a[k]) { R = k; break; }
				int ls = i - L - 1, rs = R - i - 1;
				int m = min(ls, rs), M = max(ls, rs);
				if (minv < m || (minv == m && maxv < M)) minv = m, maxv = M, s = i;
			}
			a[s] = 1;
		}
		static int tc = 0;
		printf("Case #%d: %d %d\n", ++tc, maxv, minv);
	}
}