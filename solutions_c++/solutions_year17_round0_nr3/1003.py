#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int T;
ll n, k, res;
priority_queue <ll> Q;
map <ll, ll> mp;

void PUSH(ll n, ll c) {
	if(!mp.count(n)) {
		Q.push(n);
	}
	mp[n] += c;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	cin >> T;
	for(int cas = 1; cas <= T; cas ++) {
		cin >> n >> k;
		while(!Q.empty()) Q.pop();
		mp.clear();
		
		PUSH(n, 1ll);
		while(!Q.empty()) {
			ll n = Q.top(); Q.pop();
			ll c = mp[n];
			
			k -= c;
			if(k <= 0) {
				res = n-1;
				break;
			}
			if(n % 2 == 0) {
				PUSH(n/2, c);
				PUSH(n/2-1, c);
			} else {
				PUSH(n/2, 2*c);
			}
		}
		
		cout << "Case #" << cas << ": " << (res+1)/2 << " " << res/2 << endl;
		
	}
	
	return 0;
}

