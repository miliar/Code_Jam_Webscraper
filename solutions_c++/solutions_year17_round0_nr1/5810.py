#include <bits/stdc++.h>
#include <typeinfo>
using namespace std;
typedef long long ll;

int main() {
	bool done;
	ll T,k,l, ans;
	string s;
	cin >> T;
	for (ll t = 1; t <= T; ++t) {
		cout << "Case #" << t <<": ";
		cin >> s >> k;
		l = s.length();
		ans = 0;
		done = false;
		for (ll i = 0; i < l; ++i) {
			if (s[i]=='-') {
				ans++;
				for (ll j = 0; j < k; ++j) {
					if (i+j>=l) {
						cout<<"IMPOSSIBLE" << endl;
						done = true;
						break;
					}
					s[i+j] = (s[i+j]=='+')?'-':'+';
				}
				// cout << s << endl;
				if (done) break;
			}
		}
		if (!done) cout << ans << endl;
	}
	
	return 0;
}