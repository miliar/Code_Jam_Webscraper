#include <cstdio>

const int MAX = 110;

int n, piece, modcnt[5];

void input() {
	scanf("%d%d", &n, &piece);

	for (int i = 0; i < 4; i++) {
		modcnt[i] = 0;
	}
	
	for (int i = 0; i < n; i++) {
		int t;
		scanf("%d", &t);
		modcnt[t % piece]++;
	}
}

int consume(int t0, int t1, int t2, int t3) {
	int ret = 0;
	while (modcnt[0] >= t0 && modcnt[1] >= t1 && modcnt[2] >= t2 && modcnt[3] >= t3) {
		modcnt[0] -= t0;
		modcnt[1] -= t1;
		modcnt[2] -= t2;
		modcnt[3] -= t3;
		ret++;
	}
	return ret;
}

void solve() {
	int ans = 0;

	if (piece == 2) {
		ans += consume(1, 0, 0, 0);
		ans += consume(0, 2, 0, 0);
	} else if (piece == 3) {
		ans += consume(1, 0, 0, 0);
		ans += consume(0, 1, 1, 0);
		ans += consume(0, 3, 0, 0);
		ans += consume(0, 0, 3, 0);
	} else if (piece == 4) {
		ans += consume(1, 0, 0, 0);
		ans += consume(0, 1, 0, 1);
		ans += consume(0, 0, 2, 0);
		ans += consume(0, 2, 1, 0);
		ans += consume(0, 0, 1, 2);
		ans += consume(0, 4, 0, 0);
		ans += consume(0, 0, 4, 0);
		ans += consume(0, 0, 0, 4);
	}

	if (modcnt[0] + modcnt[1] + modcnt[2] + modcnt[3] > 0) {
		ans++;
	}

	printf("%d\n", ans);
}

int main() {
	freopen("output.txt", "w", stdout);

	int numCase;
	scanf("%d", &numCase);
	for (int nowCase = 1; nowCase <= numCase; nowCase++) {
		input();

		printf("Case #%d: ", nowCase);
		solve();
	}

	return 0;
}