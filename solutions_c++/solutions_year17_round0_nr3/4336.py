#include <bits/stdc++.h>

using namespace std;

int n,k;

int main(){
	int T;
	scanf("%d",&T);
	for (int ti=1;ti<=T;ti++){
		scanf("%d%d",&n,&k);
		priority_queue<int> q;
		q.push(n);
		int ans;
		for (int i=0;i<k;i++){
			ans = q.top();
			q.pop();
			ans--;
			q.push(ans/2);
			q.push(ans-ans/2);
		}
		int x = ans/2;
		int y = ans-x;
		printf("Case #%d: %d %d\n", ti, max(x, y), min(x, y));

	}
	return 0;
}
