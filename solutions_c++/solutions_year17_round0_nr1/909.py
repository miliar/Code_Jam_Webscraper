#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll TC, K;
string S;
ll t[1005];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> TC;
	
	for (ll tc = 1; tc <= TC; tc++) {
		cin >> S >> K;
		for (ll i = 0; i < S.length(); i++) {
			if (S[i] == '+') t[i] = 1;
			else t[i] = 0;
		}


		ll ans = 0;
		for (ll i = 0; i < S.length() - K + 1; i++) {
			if (!t[i]) {
				for (ll j = i; j < i+K; j++) {
					t[j] = 1 - t[j];
				}
				ans++;
			}
		}

		bool fail = false;
		for (ll i = 0; i < S.length(); i++) {
			if (t[i] != 1) {
				fail = true;
				break;
			}
		}

		cout << "Case #" << tc << ": ";
		if (fail) cout << "IMPOSSIBLE\n";
		else cout << ans << "\n";
	}

	return 0;
}
