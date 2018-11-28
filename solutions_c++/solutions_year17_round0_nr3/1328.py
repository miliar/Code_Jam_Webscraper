#include <iostream>
#include <queue>
#define LL long long
#define PLL pair<LL,LL>
using namespace std;

PLL solve(LL N, LL K) {
	priority_queue<PLL> q;
	q.push(make_pair(N, 1));
	while (K) {
		PLL x = q.top();
		q.pop();
		while (!q.empty() && q.top().first == x.first) {
			x.second += q.top().second;
			q.pop();
		}
		if (x.second > K) {
			return make_pair(x.first / 2, (x.first - 1) / 2);
		}
		if (x.first % 2 == 1) {
			q.push(make_pair(x.first / 2, x.second * 2));
		}
		else {
			q.push(make_pair(x.first / 2, x.second));
			q.push(make_pair((x.first - 1) / 2, x.second));
		}
		K -= x.second;
	}
	if (q.empty())
		return make_pair(0, 0);
	else {
		PLL x = q.top();
		return make_pair(x.first / 2, (x.first - 1) / 2);
	}
}

int main() {
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		LL N, K;
		cin >> N >> K;

		PLL res = solve(N, --K);

		cout << "Case #" << t << ": " << res.first << " " << res.second << endl;
	}

	return 0;
}
