#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int TC;
int N, P;
int R[51];
int Q[51][51];

int solve() {
	int ans = 0;
	int X[51] = {0};
	int k = ceil(Q[0][0] / (1.1 * R[0])) - 1;
	while (true) {
		bool ok = true;
		for (int i = 0; i < N; ++i) {
			if (11 * R[i] * k < 10 * Q[i][X[i]]) {
				k++;
				ok = false;
				break;
			}
			while (9 * R[i] * k > 10 * Q[i][X[i]]) {
				X[i]++;
				ok = false;
				if (X[i] >= P) return ans;
			}
		}
		if (ok) {
			ans++;
			for (int i = 0; i < N; ++i) {
				X[i]++;
				if (X[i] >= P) return ans;
			}
		}
	}
	return ans;
}

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; ++tc) {
		scanf("%d%d", &N, &P);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &R[i]);
		}
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < P; ++j) {
				scanf("%d", &Q[i][j]);
			}
			sort(&Q[i][0], &Q[i][P]);
		}
		printf("Case #%d: %d\n", tc, solve());
	}
	return 0;
}

