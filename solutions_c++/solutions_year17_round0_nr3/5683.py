#include <cstdio>
#include <queue>
using namespace std;
int main() {
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int N, K;
		scanf("%d%d", &N, &K); --K;
		priority_queue<int> heap;
		heap.push(N);
		int x;
		while (K--) {
			x = heap.top(); heap.pop();
			heap.push((x - 1) / 2);
			heap.push(x / 2);
		}
		x = heap.top();
		printf("Case #%d: %d %d\n", t, x / 2, (x - 1) / 2);
	}
	return 0;
}