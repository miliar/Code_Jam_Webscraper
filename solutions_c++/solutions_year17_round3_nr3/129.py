#include<bits/stdc++.h>

using std::vector;
using std::greater;


int main() {
	int tc;
	scanf("%d", &tc);
	int T = 0;
	while (tc--) {
		int n, k;
		scanf("%d%d", &n,&k);
		int sum = 0;
		int a, b;
		scanf("%d.%d", &a, &b);
		sum += a * 10000 + b;
		std::priority_queue<int, vector<int>, greater<int>> heap;
		for (int i = 0; i < n; i++) {
			scanf("%d.%d", &a, &b);
			heap.push(a * 10000 + b);
		}
		for (int i = 0; i < sum; i++) {
			int p = heap.top();
			heap.pop();
			p++;
			heap.push(p);
		}
		double ans = 1;
		while (!heap.empty()) {
			double p = std::min(heap.top(),10000);
			p /= 10000;
			ans *= p;
			heap.pop();
		}
		T++;
		printf("Case #%d: %.10lf\n", T, ans);
	}
}