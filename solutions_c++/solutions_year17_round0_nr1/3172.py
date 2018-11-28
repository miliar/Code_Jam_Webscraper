#include <bits/stdtr1c++.h>

using namespace std;

typedef long double ld;
typedef long long ll;
typedef pair<ll, ll> pii;
typedef complex<ld> pt;

int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int ca = 1; ca <= t; ca++) {
		int k;
		string s; cin >> s >> k;
		int ans = 0;
		for (int i = 0; i < s.size(); i++) {
			if (i+k <= s.size()) {
				if (s[i] == '-') {
					for (int j = i; j < i+k; j++) {
						s[j] ^= '-'^'+';
					}
					ans++;
				}
			}
			if (s[i] == '-') ans = -1;
		}
        cout << "Case #" << ca << ": ";
		
		if (ans == -1) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
    }
	return 0;
}