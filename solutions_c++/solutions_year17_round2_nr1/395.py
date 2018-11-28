#include <cstdio>
#include <algorithm>

using namespace std;

typedef pair < int, int > pii;

const int MAX = 1020;

int dist, n;
pii horses[MAX];

void input() {
	scanf("%d%d", &dist, &n);
	for (int i = 0; i < n; i++) {
		scanf("%d%d", &horses[i].first, &horses[i].second);
	}
}

void solve() {
	double ans = 1e50;

	for (int i = 0; i < n; i++) {
		double time = (double)(dist - horses[i].first) / horses[i].second;
		double cand = dist / time;
		ans = min(cand, ans);
	}

	printf("%.10lf\n", ans);
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