#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 1005, MAXC = 1005, MAXM = 1005;
int N, C, M, P[MAXM], B[MAXM];
int cSeat[MAXN], cPerson[MAXC], ans1, ans2;

void solve() {
	ans1 = 0;
	for (int i = 1; i <= C; ++i)
		ans1 = max(ans1, cPerson[i]);
	int sum = 0;
	for (int i = 1; i <= N; ++i) {
		sum += cSeat[i];
		ans1 = max(ans1, (sum + i - 1) / i);
	}
	printf("%d ", ans1);
	int remain = 0;
	ans2 = 0;
	sum = 0;
	for (int i = 1; i <= N; ++i) {
		sum += cSeat[i];
		if (cSeat[i] > ans1)
			ans2 += cSeat[i] - ans1;
	}
	printf("%d\n", ans2);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d%d%d", &N, &C, &M);
		for (int i = 1; i <= N; ++i) cSeat[i] = 0;
		for (int i = 1; i <= C; ++i) cPerson[i] = 0;
		for (int i = 1; i <= M; ++i)
			scanf("%d%d", &P[i], &B[i]), ++cSeat[P[i]], ++cPerson[B[i]];
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}
