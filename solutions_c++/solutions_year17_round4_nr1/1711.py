#include <cstdio>

using namespace std;

int N, P;
int D[5];

int solve();

int main() {
	int tc;

	scanf("%d", &tc);
	for (int t = 1; t <= tc; ++t) {
		scanf("%d %d", &N, &P);
		for (int i = 0; i < P; ++i) D[i] = 0;
		for (int i = 0; i < N; ++i) {
			int x;
			scanf("%d", &x);
			++D[x % P];
		}

		const int ans = solve();
		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}

int solve() {
	if (P == 2) {
		return D[0] + (D[1] + 1) / 2;
	}

	else if (P == 3) {
		int cnt = 0;
		while (D[1] > 0 && D[2] > 0) {
			++cnt;
			--D[1];
			--D[2];
		}

		return D[0] + cnt + (D[1] + D[2] + 2) / 3;
	}

	return 0;
}