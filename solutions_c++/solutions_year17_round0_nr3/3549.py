#include<bits/stdc++.h>
#define rep(i,n)for(int i=0;i<(n);i++)
using namespace std;

int main() {
	int T; scanf("%d", &T);
	for (int cnt = 1; cnt <= T; cnt++) {
		int n, k; scanf("%d%d", &n, &k);
		priority_queue<int>que; que.push(n);
		rep(i, k - 1) {
			int p = que.top(); que.pop();
			int a = (p - 1) / 2;
			que.push(a); que.push(p - 1 - a);
		}
		int a = (que.top() - 1) / 2;
		printf("Case #%d: %d %d\n", cnt, que.top() - 1 - a, a);
	}
}