#include <bits/stdc++.h>
using namespace std;
int t,n,k,l,r;
priority_queue<int> q;
int main() {

	scanf("%d",&t);
	for (int tc = 1; tc <= t; ++tc){
		scanf("%d %d",&n,&k);
		while (!q.empty()) q.pop();
		q.push(n);
		while (k--){
			int m = q.top();
			q.pop();
			l = (m-1)/2;
			r = m-1 - l;

			q.push(l);
			q.push(r);
						//cout << m << " " << l << " " << r << endl;
		}
		printf("Case #%d: %d %d\n", tc, max(l,r), min(l,r));

	}
}