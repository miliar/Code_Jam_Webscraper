#include <bits/stdc++.h>
using namespace std;

int T;

int main() {
	scanf("%d", &T);
	for(int t=0; t<T; t++){
		int n, k;
		scanf("%d %d", &n, &k);
		priority_queue<int> q;
		q.push(n);
		for(int i=0; i<k-1; i++){
			int v = q.top() - 1;
			q.pop();
			int b = v / 2,
				a = v / 2 + v % 2;
			//printf("%d %d %d\n", v, a, b);
			if(a > 0)
				q.push(a);
			if(b > 0)
				q.push(b);
		}
		int v = q.top() - 1;
		printf("Case #%d: %d %d\n", t+1, max(v / 2, v / 2 + v % 2), v / 2);
	}
}
