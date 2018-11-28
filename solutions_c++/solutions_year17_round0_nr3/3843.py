#include <bits/stdc++.h>
using namespace std;
int main()
{
	int T;
	scanf("%d", &T);
	for(int t=1;t<=T;t++){
		int n, k;
		scanf("%d%d", &n, &k);
		priority_queue<int>pq;
		pq.push(n);
		for(int i=1;i<=k;i++){
			int tmp=pq.top();
			pq.pop();
			int ma=tmp/2;
			int mi=(tmp-1)/2;
			pq.push(ma);
			pq.push(mi);
			if(i==k){
				printf("Case #%d: %d %d\n", t, ma, mi);
			}
		}
	}
}

