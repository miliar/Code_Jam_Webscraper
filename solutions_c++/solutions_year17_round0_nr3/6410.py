#include <algorithm>
#include <cstdio>
#include <cstring>
#include <queue>

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; ++t) {
		int n, m;
		scanf("%d%d", &n, &m);
		std::priority_queue<int> heap;
		heap.push(n);
		int left = 0, right = 0;
		while (m--) {
			int length = heap.top();
			heap.pop();
			left = length / 2;
			right = length - 1 - left;
			heap.push(left);
			heap.push(right);
		}
		printf("Case #%d: %d %d\n", t, left, right);
	}
	return 0;
}