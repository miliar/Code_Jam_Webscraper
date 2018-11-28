#include <bits/stdc++.h>

using namespace std;



int main(){
	int t, n, k;
	scanf("%d", &t);
	for(int x=1; x<=t; x++){
		scanf("%d%d", &n, &k);
		priority_queue<int, vector<int>, less<int> > pq;
		int l, r;
		l = n/2;
		r = (n-1)/2;
		pq.push(l);
		pq.push(r);
		for(int i=0; i<k-1; i++){
			l = pq.top()/2;
			r = (pq.top()-1)/2;
			pq.push(l);
			pq.push(r);
			pq.pop();
		}
		printf("Case #%d: %d %d\n", x, l, r);
	}
	return 0;
}