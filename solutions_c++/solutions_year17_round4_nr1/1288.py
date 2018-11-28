#include <bits/stdc++.h>
using namespace std;

const int MOD = int(1e9 + 7);

int N, P;
int x[6];

void solve() {
	scanf("%d%d", &N, &P);
	memset(x, 0, sizeof x);
	for (int i = 0; i < N; i++) {
		int u;
		scanf("%d", &u);
		x[u%P]++;
	}
	int res = 0, all = N, left = 0;
	while (all > 0) {
		// find fit
		if (x[(P-left)%P] > 0) {
			all--;
			res += (left == 0);
			x[(P-left)%P]--;
			left = 0;
			continue;
		}
		// find group with max number
		int g = 1;
		for (int i = 1; i < P; i++) if (x[i] > x[g])
			g = i;
		// assign that number
		res += (left == 0);
		x[g]--;
		all--;
		left = (left + g) % P;
	}
	printf("%d\n", res);
}

int main() {
	freopen("A.out", "w", stdout);
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}