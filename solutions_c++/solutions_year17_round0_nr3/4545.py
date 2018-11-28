/******************************************
*    AUTHOR:         BHUVNESH JAIN        *
*    INSTITUITION:   BITS PILANI, PILANI  *
******************************************/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL; 
typedef long double LD;
typedef pair<int,int> pii;
typedef pair<LL, LL> pll;

int main() {
	ios_base::sync_with_stdio(false);
	int t, n, k;
	int a, b, c;
	cin >> t;
	for(int T = 1; T <= t; ++T) {
		cout << "Case #" << T << ": ";
		
		cin >> n >> k;
		priority_queue<int> pq;
		pq.push(n);
		int ctr = 0;
		a = b = 0;
		while(!pq.empty()) {
			ctr += 1;
			c = pq.top();
			pq.pop();
			a = c/2;
			b = (c-1)/2;
			if (k == ctr) {
				cout << a << " " << b << "\n";
				break;
			}
			if (a > 1) {
				pq.push(a);
			}
			if (b > 1) {
				pq.push(b);
			}
		}
		if (ctr < k) {
			a = b = 0;
			cout << a << " " << b << "\n";
		}
	}
	return 0;
}