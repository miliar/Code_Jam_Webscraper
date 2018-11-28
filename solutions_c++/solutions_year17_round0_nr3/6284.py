#include <iostream>
#include <queue>
using namespace std;

int main(void){
	int t; cin >> t;
	for(int tt = 1; tt <= t; tt++){

		int n; cin >> n;
		priority_queue<int> pq;
		pq.push(n);
		int k; cin >> k;
		while(--k){
			int x = pq.top(); pq.pop();
			if(x / 2 != 0) pq.push(x / 2);
			if((x - 1) / 2 != 0) pq.push((x-1) / 2);
		}
		int ans = pq.top();	
		cout << "Case #" << tt << ": ";
		cout << ans / 2 << " " << (ans - 1) / 2 << endl;
	}
	return 0;
}
