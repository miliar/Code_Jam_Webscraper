#include <cstdio>
#include <queue>
#include <utility>

using namespace std;

// Small 1, 2
pair<int,int> solve(int, int);

int main() {
	int tc;
	scanf("%d", &tc);

	for (int t = 1; t <= tc; ++t) {
		int n, k;
		scanf("%d %d", &n, &k);

		auto ans = solve(n, k);
		printf("Case #%d: %d %d\n", t, ans.first, ans.second);
	}

	return 0;
}

pair<int,int> solve(int N, int K) {
	priority_queue<pair<int, int> > pq;

	pq.emplace(N, -0);
	for (int t = 1; t < K; ++t) {
		const int sz = pq.top().first;
		const int lt = -pq.top().second;
		pq.pop();

		if (sz % 2) {
			if (sz >= 3) {
				pq.emplace(sz / 2, -(lt));
				pq.emplace(sz / 2, -(lt + sz / 2));
			}
		} else {
			if (sz >= 2) {
				if (sz >= 4) pq.emplace(sz / 2 - 1, -(lt));
				pq.emplace(sz / 2, -(lt + sz / 2 - 1));
			}
		}
	}

	return {pq.top().first / 2, (pq.top().first - 1) / 2};
}