#include <iostream>
#include <string>

using namespace std;
typedef long long ll;

int main() {
	ll t;
	cin >> t;
	for (ll i = 1; i <= t; i++) {
		string s;
		cin >> s;
		ll K, ans = 0;
		cin >> K;
		ll l = s.length();
		for (ll j = 0; j < l; j++) {
			if (s[j] == '-' && ((j + K - 1) <= (l - 1))) {
				for (ll k = j; k <= j + K - 1; k++) {
					s[k] = ((s[k] == '+') ? '-':'+');
				}
				++ans;
			}
		}
		for (ll j = 0; j < l; j++) {
			if (s[j] == '-') {
				ans = -1;
				break;
			}
		}
		cout << "Case #" << i << ": ";
		if (ans == -1) {
			cout << "IMPOSSIBLE\n";
		} else {
			cout << ans << "\n";
		}
	}
	return 0;
}

/*
-+-+-
+-+--
++-+-


--+--++++ 4
++-+-++++
+++-+-+++
++-+-++++

++--++--- 5
++-++ 2 np
+--++ 2 1
+---++-+ 2 4
+++-++-+
++++-+-+
+++++--+


*/