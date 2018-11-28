#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long ll;
typedef long double ld;
typedef complex<ld> pt;
const int MOD = 1e9 + 7;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		ll N; cin >> N;
		string s = to_string(N);
		for (int i = 0; i < s.length()-1; i++) {
			if (s[i] > s[i+1]) {
				s[i]--;
				for (int j = i+1; j < s.length(); j++) {
					s[j] = '9';
				}
				i = -1;
			}
		}
		ll ans = stoll(s);
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}