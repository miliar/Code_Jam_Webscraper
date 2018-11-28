#include<bits/stdc++.h>


int dy[101][101][101][4];
int p = 0;
int go(int a, int b, int c,int d) {
	if (a == 0 && b == 0 && c == 0) {
		return 0;
	}
	auto& ret = dy[a][b][c][d];
	if (ret != -1) {
		return ret;
	}
	if (a != 0) {
		ret = std::max(ret, go(a - 1, b, c, (d + 1) % p));
	}
	if (b != 0) {
		ret = std::max(ret, go(a, b - 1, c, (d + 2) % p));
	}
	if (c != 0) {
		ret = std::max(ret, go(a, b , c-1, (d + 3) % p));
	}
	if (d == 0) {
		ret++;
	}
	return ret;
}


int main() {
	int tc;
	scanf("%d", &tc);
	int T = 0;
	while (tc--) {
		memset(dy, 0xff, sizeof(dy));
		int n;
		int cnt[4] = { 0, };
		scanf("%d%d", &n, &p);
		for (int i = 0; i < n; i++) {
			int a;
			scanf("%d", &a);
			cnt[a % p]++;
		}
		T++;
		printf("Case #%d: %d\n", T, go(cnt[1], cnt[2], cnt[3], 0) + cnt[0]);
	}
}