#include <stdio.h>
#include <queue>

using namespace std;

priority_queue<int> pq;

void solve(int n, int k) {
	while (!pq.empty()) {
		pq.pop();
	}
	pq.push(n);
	int ls, rs;
	for (int i = 0; i < k; ++i) {
		int cur = pq.top();
		pq.pop();
		if (cur & 1) {
			pq.push(cur / 2);
			pq.push(cur / 2);
			ls = rs = cur / 2;
		} else {
			pq.push(cur / 2);
			pq.push(cur / 2 - 1);
			ls = cur / 2;
			rs = cur / 2 - 1;
		}
	}
	printf("%d %d\n", ls, rs);
}

int main() {
	freopen("C-small-2-attempt1.in", "r", stdin);
	freopen("C-small-2-attempt1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		int n, k;
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", i);
		solve(n, k);
	}
	return 0;
}
