#include <bits/stdc++.h>

using namespace std;

int main() {
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	long long int m,k,ak;
	
	int n;
	cin >> n;
	for(int zzzz=0;zzzz<n;zzzz++) {	
		priority_queue<long long int> pq;	
		cin >> m >> k;
		pq.push(m);
		for(int i=0;i<k-1;i++) {
			ak = pq.top();
			pq.pop();
			if(ak % 2) {
				pq.push(ak/2);
				pq.push(ak/2);
			} else {
				pq.push(ak/2 - 1);
				pq.push(ak/2);
			}
		}
		ak = pq.top();
		pq.pop();
		if(ak % 2) {
			cout << "Case #" << zzzz+1 << ": " << ak/2 << ' ' << ak/2 << '\n';
		} else {
			cout << "Case #" << zzzz+1 << ": " << ak/2 << ' ' << ak/2 - 1<< '\n';
		}
	}
	
	return 0;
}
