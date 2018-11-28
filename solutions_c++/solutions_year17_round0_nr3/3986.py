#include<bits/stdc++.h>
using namespace std;

int n, k, T;

int main(){
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("x.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t){
		printf("Case #%d: ", t);
		scanf("%d%d", &n, &k);
		priority_queue<int> q;
		q.push(n);
		while(k > 1){
			int x = q.top();
			q.pop();
			q.push(x / 2);
			q.push((x - 1) / 2);
			k--;
		}
		int x = q.top();
		printf("%d %d\n", x / 2, (x - 1) / 2);
	}
	return 0;
}
