#include <bits/stdc++.h>

using namespace std;

#define INF 2000000000
#define MOD 1000000007
typedef long long ll;
typedef pair<int, int> P;


int main()
{
	int t;
	cin >> t;
	for (int ii = 1; ii <= t; ii++) {
		ll n, k;
		cin >> n >> k;
		ll mx, mi;
		priority_queue <ll> pq; // default 大きい順
		pq.push(n);

		for (int i = 0; i < k; i++) {
			ll tmp = pq.top(); pq.pop();
			if (tmp%2==0) {
				pq.push(tmp/2);
				pq.push(tmp/2-1);
				mx = tmp/2;
				mi = tmp/2-1;
			} else {
				pq.push(tmp/2);
				pq.push(tmp/2);
				mx = tmp/2;
				mi = tmp/2;
			}
		}
		cout << "Case #" << ii << ": " << mx << " " << mi << "\n";
	}
}
