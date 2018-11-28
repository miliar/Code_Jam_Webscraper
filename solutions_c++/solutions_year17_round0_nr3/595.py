#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

pair<LL, LL> partition(LL x) {
	LL half = x / 2;
	LL otherHalf = x - 1 - half;

	return {half, otherHalf};
}

pair<LL, LL> solve(LL n, LL k) {
	priority_queue<pair<LL, LL>> pq;
	map<LL, LL> dp;

	dp[n] = 1;
	pq.push({n, 1});

	while(!pq.empty()) {
		LL cur = pq.top().first;
		LL val = pq.top().second;
		pq.pop();

		if(dp[cur] != val) continue;
		// cout << cur << " " << val << "\n";
		if(val >= k) {
			return partition(cur);
		} else {
			k -= val;
		}

		pair<LL, LL> child = partition(cur);

		dp[child.first] += val;
		dp[child.second] += val;

		pq.push({child.first, dp[child.first]});
		if(child.first != child.second)
			pq.push({child.second, dp[child.second]});
	}

	assert(false);
}

int main() {
	int t; cin >> t;
	for(int tc = 1 ; tc <= t ; tc++) {
		LL n, k;
		cin >> n >> k;

		pair<LL, LL> ret = solve(n, k);
		printf("Case #%d: %lld %lld\n", tc, ret.first, ret.second);
	}
	return 0;
}