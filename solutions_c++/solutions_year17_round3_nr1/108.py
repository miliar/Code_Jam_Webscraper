#include <stdio.h>
#include <functional>
#include <vector>
#include <algorithm>
#include <string.h>
#include <assert.h>
#include <limits.h>
#include <queue>
#include <string>
#include <iostream>
#include <cmath>

using namespace std;
typedef long long ll;
const double PI = acos(-1);

ll r[1001], h[1001];
ll solve() {
	int K, N; scanf("%d %d", &N, &K);
	for (int i = 0; i < N; i++) {
		scanf("%lld %lld", &r[i], &h[i]);
	}

	ll ans = 0;
	for (int i = 0; i < N; i++) {
		ll now = 0;
		now += r[i] * r[i];
		now += 2LL * r[i] * h[i];
		
		vector<ll> candidates;
		for (int j = 0; j < N; j++) {
			if (i == j) continue;
			candidates.push_back(r[j] * h[j]);
		}
		sort(candidates.begin(), candidates.end());
		for (int j = N-1 - (K - 1); j < N-1; j++) {
			now += 2 * candidates[j];
		}
		if (ans < now) {
			ans = now;
		}
	}
	return ans;
}

int main(void) {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T; scanf("%d\n", &T);
	
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		

		
		printf("%.10lf\n", PI * double(solve()));
	}

}