#include <bits/stdc++.h>

using namespace std;



int main(){
	int t;
	cin >> t;

	int f = 0;
	while(t--){
		int n, k;
		cin >> n >> k;
		priority_queue<int> pq;
		pq.push(n);
		k--;
		while(k--){
			auto u = pq.top();
			pq.pop();
	
			pq.push(u/2);

			if(u%2){
				pq.push(u/2);
			} else {
				pq.push(u/2 - 1);
			}
		}
		
		printf("Case #%d: %d %d\n", ++f, pq.top()/2, pq.top()%2 ? pq.top()/2 : pq.top()/2 - 1);
	}
}
