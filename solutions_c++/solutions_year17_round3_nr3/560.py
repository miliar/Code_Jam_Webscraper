#include <algorithm>
#include <cmath>
#include <cassert>
#include <cstdio>
#include <utility>
#include <vector>

using namespace std;

#define REP(i,b) for (int i = 0; i < (b); i++)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)

struct Segment { int from, to, who; };
bool operator<(const Segment &a, const Segment &b) { return a.from < b.from; }

int read_prob() {
	double d;
	scanf("%lf", &d);
	return (int) round(d * 10000);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int N, K;
		scanf("%d%d", &N, &K);
		int U = read_prob();
		vector<int> P(N);
		REP(i, N) P[i] = read_prob();

		while (U > 0) {
			int lowest = -1;
			REP(i, N) {
				if (lowest == -1 || P[i] < P[lowest]) {
					lowest = i;
				}
			}
			if (P[lowest] >= 10000) break;
			P[lowest]++;
			U--;
		}

		double ans = 1.0;
		REP(i, N) {
			ans *= P[i] / 10000.0;
		}
		printf("Case #%d: %lf\n", tc, ans);
	}
	return 0;
}
