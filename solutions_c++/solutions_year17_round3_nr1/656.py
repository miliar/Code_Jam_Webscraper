#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;

const double pi = 3.1415926535;

struct pan {
	int r, h;
} panck[1001000];

bool cmp(const pan &a, const pan &b) {
	return a.r < b.r;
}

double S[1001000];
int N, K, T;

int main() {
	scanf("%d", &T);
	for (int TT = 1; TT <= T; TT++) {
		printf("Case #%d: ", TT);

		scanf("%d%d", &N, &K);
		for (int i = 1; i <= N; i++) {
			scanf("%d%d", &panck[i].r, &panck[i].h);
		}

		sort(&panck[1], &panck[N + 1], cmp);

		double maxx = 0;
		double ans = 0;
		std::priority_queue<double, vector<double>, greater<double>> Q;
		for (int i = 1; i <= N; i++) {
			S[i] = 2 * pi * panck[i].r * panck[i].h;
			maxx += S[i];
			if (Q.size() == K - 1) {
				ans = max(ans, maxx + pi * panck[i].r * panck[i].r);
			}
			Q.push(S[i]);
			if (Q.size() >= K) {
				maxx -= Q.top();
				Q.pop();
			}
		}
		printf("%.8f\n", ans);
	}

	return 0;
}