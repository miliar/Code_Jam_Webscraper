#include <bits/stdc++.h>

using namespace std;

pair<int, int> calc(int n, int k) {
	priority_queue<int> pq;
	pq.push(n);
	for (int i = 1; i < k; ++i) {
		int u = pq.top();
		pq.pop();
		int x = (u + 1) >> 1;
		pq.push(x - 1);
		pq.push(u - x);
	}
	int u = pq.top();
	int x = (u + 1) >> 1;
	return {u - x, x - 1};
}

int main() {
	int t, n, k;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		scanf("%d %d", &n, &k);
		pair<int, int> ans = calc(n, k);
		printf("Case #%d: %d %d\n", tc, ans.first, ans.second);
	}
	return 0;
}