#include <bits/stdc++.h>
using namespace std;
int n, k;
int main(int argc, const char* agrv[]) {
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, ca = 1;
	scanf("%d", &T);
	while(T--) {
		scanf("%d %d", &n, &k);
		priority_queue<int> q;
		q.push(n);
		for(int i = 1; i < k; ++i) {
			int u = q.top(); q.pop();
			q.push((u-1)/2);
			q.push(u/2);
		}
		int u = q.top();
		printf("Case #%d: %d %d\n", ca++, u/2, (u-1)/2);
	}
}

