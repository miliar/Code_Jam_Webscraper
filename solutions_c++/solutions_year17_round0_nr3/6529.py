#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <queue>
using namespace std;
int tc, n, k;

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	cin >> tc;
	for(int i = 1; i <= tc; i++) {
		printf("Case #%d: ", i);
		cin >> n >> k;
		priority_queue<int> pq;
		pq.push(n);
		int x = 0, y = 0;
		for(int j = 0; j < k; j++) {
			int len = pq.top() - 1;
			pq.pop();
			x = len / 2;
			y = (len + 1) / 2;
			pq.push(x);
			pq.push(y);
		}
		printf("%d %d\n", y, x);
	}
	return 0;
}