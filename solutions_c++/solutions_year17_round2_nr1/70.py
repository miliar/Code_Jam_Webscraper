#include <bits/stdc++.h>
using namespace std;

const int MOD = int(1e9 + 7);

void solve() {
	int D, N;
	scanf("%d%d", &D, &N);
	double t = 0;
	for (int i = 0; i < N; i++) {
		int K, S;
		scanf("%d%d", &K, &S);
		t = max(t, 1.0*(D-K)/S);
	}
	printf("%.7f\n", 1.0*D/t);
}

int main() {
	freopen("A.out", "w", stdout);
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}