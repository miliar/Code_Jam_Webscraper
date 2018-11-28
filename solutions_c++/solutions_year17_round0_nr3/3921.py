#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <queue>

using namespace std;

const int MXN = 1000010;

struct node {
	int x;
	node() {}
	node(int x) : x(x) {}
	bool friend operator < (node a, node b) {
		return a.x < b.x;
	}
};
int T, n, K;
priority_queue <node> q;
inline void solve() {
	scanf("%d", &T);
	for(int ii = 1; ii <= T; ii++) {
		scanf("%d%d", &n, &K);
		while(!q.empty()) q.pop();
		//printf("%d\n", ii);
		q.push(node(n));
		int nowwmin, nowwmax;
		for(int i = 1; i <= K; i++) {
			node u = q.top(); q.pop();
			if(u.x & 1) nowwmin = u.x / 2;
			else nowwmin = u.x / 2 - 1; //
			nowwmax = u.x - 1 - nowwmin; //
			q.push(node(nowwmin));
			q.push(node(nowwmax));
		}
		printf("Case #%d: %d %d\n", ii, nowwmax, nowwmin);
	}
}
int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w",stdout);
	solve();
	return 0;
}
