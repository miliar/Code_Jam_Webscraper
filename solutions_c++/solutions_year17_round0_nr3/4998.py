#include <bits/stdc++.h>

#define N 1000007
#define it(i, n) for(i = 0; i < n; ++i)
#define pb push_back
#define eps 1e-9
#define all(x) x.begin(), x.end() 

using namespace std;
typedef long long ll;

int main(int argc, char * argv[]) {
	int i, j, k, m, p, q, r, t;
	ll n, res;

	priority_queue<ll> pq;

	cin >> t;
	it(i, t) { 
		cin >> n >> k;
		printf("Case #%d: ", i+1);

		res = 0;
		pq.push(n);
		while(!pq.empty()) {
			k--;
			ll next = pq.top();
			pq.pop();
			if(!k) {
				res = next;
				break;
			}
			pq.push(next/2);
			pq.push(next - next/2 - 1);
		}
		while(!pq.empty()) pq.pop();
		if(res >= 2) cout << res/2 << " " << res - (res/2) - 1 << endl;
		else cout << 0 << " " << 0 << endl;
	}

	return 0;
}