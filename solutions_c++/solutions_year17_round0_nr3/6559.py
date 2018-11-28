#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, k, ans;
		scanf("%d %d", &n, &k);
		
		priority_queue<int> q;
		q.push(n);
		while (k--) {
			ans = q.top();
			q.pop();
			
			int m = (ans - 1) / 2;
			
			if (m > 0) q.push(m);
			if (m < ans - 1) q.push(ans - 1 - m);
		}
		
		printf("Case #%d: %d %d\n", t, ans / 2, (ans - 1) / 2);
	}
	
	return 0;
}
