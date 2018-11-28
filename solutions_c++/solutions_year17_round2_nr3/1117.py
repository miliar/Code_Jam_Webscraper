#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cstdio>
using namespace std;

const double inf = 1e300;
const long long MAXN = 101;
long long field[MAXN][MAXN];

long long N, Q;
long long maxDist[MAXN];
long long speed[MAXN];

double getResult() {
	double dp[MAXN];
	dp[1] = 0.0;

	for (long long i = 2; i <= N; i++) {
		dp[i] = inf;
		long long dist = 0;

		for (long long j = i - 1; j > 0; j--) {
			dist += field[j][j + 1];

			if (dist <= maxDist[j]) {
				dp[i] = min(dp[i], dp[j] + (double)dist / speed[j]);
			}
		}
	}

	return dp[N];
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c-small.out", "w", stdout);

	long long nCases;
	cin >> nCases;

	for (long long cnt = 1; cnt <= nCases; cnt++) {
		cin >> N >> Q;

		for (long long i = 1; i <= N; i++) {
			cin >> maxDist[i] >> speed[i];
		}

		for (long long i = 1; i <= N; i++) {
			for (long long j = 1; j <= N; j++) {
				cin >> field[i][j];
			}
		}

		for (long long i = 1; i <= Q; i++) {
			long long x, y;
			cin >> x >> y;
		}

		cout << fixed << setprecision(8);
		cout << "Case #" << cnt << ": " << getResult() << endl;
	}

	return 0;
}