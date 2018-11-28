#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

using ll = long long;

void solve() {
	int D, N;
	scanf("%d%d", &D, &N);
	double ans = 1e30;
	for (int i = 0; i < N; ++i) {
		int k, s;
		scanf("%d%d", &k, &s);
		double newSpeed = 1.*D*s / (D - k);
		ans = min(ans, newSpeed);
	}
	printf("%.10lf\n", ans);
}

int main() {
	freopen("ain.txt", "r", stdin);
	freopen("aout.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		fprintf(stderr, "%d\n", i + 1);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}