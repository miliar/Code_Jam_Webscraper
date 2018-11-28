#include<stdlib.h>
#include<stdio.h>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;

int main(){
    freopen("C-small-2-attempt0.in","rt",stdin);
	freopen("C-small-2-attempt0.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		int n, k;	scanf("%d%d", &n, &k);
		priority_queue<int> pq; pq.push(n);
		int u, l, r;
		for (int i = 0; i < k; i++){
			u = pq.top(); pq.pop();
			l = (u - 1) / 2, r = u / 2;
			pq.push(l), pq.push(r);
		}
		printf("Case #%d: %d %d\n", tc, max(l, r), min(l, r));
	}
}
