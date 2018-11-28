#define boost ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define mod 1000000007
#define INF LLONG_MAX
#include <unordered_set>
#include<bits/stdc++.h>
#include<unordered_map>
using namespace std;
#define ll long long

int main() {

	boost;
	freopen("inp.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ll t;
	cin >> t;
	for (ll ccr = 1; ccr <= t; ++ccr) {

		ll n, k, val1, val2;
		cin >> n >> k;
		priority_queue<ll> pq; unordered_map<ll, ll> hm;
		pq.push(n);
		hm[n] = 1;
		--k;
		while (k>0) {
			ll val = pq.top();
			
			if (k >= hm[val]) {
				val1 = val2 = val / 2;
				pq.pop();
				k -= hm[val];
				if (val % 2 == 0) {
					--val2;

					if (hm.find(val1) == hm.end()) {
						pq.push(val1);
					}
					hm[val1] += hm[val];

					if (hm.find(val2) == hm.end()) {
						pq.push(val2);
					}
					hm[val2] += hm[val];
					hm.erase(val);
				}
				else {
					if (hm.find(val1) == hm.end()) {
						pq.push(val1);
					}
					hm[val1] += 2 * hm[val];
					hm.erase(val);
				}
			}
			else {
				k = 0;
				break;
			}
		}
		ll gap = pq.top();
		val1 = val2 = gap / 2;
		if (gap % 2 == 0)
			--val2;
		cout << "Case #" << ccr << ": " << val1 << " " << val2 << "\n";
	}
	return 0;
}