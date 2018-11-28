#include <bits/stdc++.h>
using namespace std;


int T;
int N, K;
int l, r;
int main() {
//	freopen("C-small-1-attempt0.in", "r", stdin);
//	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		//queue<int> q;
		priority_queue<int> q;
		scanf("%d %d", &N, &K);
		q.push(N);
		for (int k = 1; k <= K; k++) {
			if (q.top() & 1) {
				l = r = q.top() / 2;
				if (l != 0) {
					q.push(l);
					q.push(r);
				}
			}
			else {
				l = q.top() / 2 - 1;
				r = q.top() / 2;
				if (r != 0)
					q.push(r);
				if (l != 0)
					q.push(l);
			}
			//cout << l << " " << r << endl;
			q.pop();
		}
		printf("Case #%d: %d %d\n", t, max(l, r), min(l, r));
	}
	return 0;
}