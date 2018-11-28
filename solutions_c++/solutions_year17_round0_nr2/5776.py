#include <bits/stdc++.h>
#include <typeinfo>
using namespace std;
typedef long long ll;

int main() {
	bool done;
	ll T,n,l,k;
	string s;
	cin >> T;
	for (ll t = 1; t <= T; ++t) {
		cout << "Case #" << t <<": ";
		cin >> n;
		s = to_string(n);
		l = s.length();
		k = 0;
		for (ll i = 0; i < l-1; ++i) {
			if (s[i]<s[i+1]) k = i+1;
			if (s[i]>s[i+1]) {
				s[k]--;
				for (ll j = k + 1; j < l; ++j) s[j] = '9';
				break;
			}
		}
		cout << stoll(s) << endl;
	}
	
	return 0;
}