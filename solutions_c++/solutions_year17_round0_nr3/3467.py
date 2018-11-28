#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
	int t;
	cin >> t;

	int c = 1;
	while (t--) {
		ll n, k;
		cin >> n >> k;

		priority_queue<ll> pq;	
		pq.push(n);

		while (k != 1) {
			ll top = pq.top();
			pq.pop();

			if (top % 2) {
				pq.push((top-1)/2);
				pq.push((top-1)/2);
			} else {
				pq.push((top-1)/2);
				pq.push((top-1)/2+1);
			}
			k--;
		}

		ll top = pq.top();
		if (top % 2) {
			cout << "Case #" << c++ << ": " << (top-1)/2 << " " << (top-1)/2 << endl;
		} else {
			cout << "Case #" << c++ << ": " << (top-1)/2+1 << " " << (top-1)/2 << endl;
		}
	}

	return 0;

}
