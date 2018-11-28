#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	int t;
	ll n, k;
	string s;
	cin >> t;
	for(int _t = 1; _t <= t; _t++) {
		cin >> n >> k;
	
		ll c = (ll) 1;
		while(k >= 4*c) {
			c *= 2;
			//cout << c << endl;
		}
		
		stack<int> st;
		while(c) {
			if(k - 2*c >= c) { st.push(1); k -= 2*c;}
			else if(k - c >= c) { st.push(0); k -= c;}
			c/=2;
		}
		
		while(!st.empty()) {
			if((st.top() % 2 == 1) && (n%2 == 0)) {
				n = n/2 - 1;
			}
			else n/=2;
			st.pop();
		}
		
		printf("Case #%d: ", _t);
		if(n%2) cout << n/2<< " " << n/2 << endl;
		else cout << n/2 << " " << (n/2-1) << endl;
	}
	return 0;
}
