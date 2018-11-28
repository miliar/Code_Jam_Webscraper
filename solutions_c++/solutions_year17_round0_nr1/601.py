#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int main() {
	ios_base::sync_with_stdio(false);

	int t;
	cin >> t;
	int kase = 1;
	while(t--) {
		string s;
		cin >> s;
		int k;
		cin >> k;
		int n = s.size();
		int ans = 0;
		fori(i, 0, n - k + 1) {
			if(s[i] == '-') {
				fori(j, i, i + k) {
					s[j] = s[j] == '+' ? '-' : '+';
				}
				ans++;
			}
		}
		for(auto &each : s) {
			if(each == '-') {
				ans = -1;
			}
		}
		cout << "Case #" << kase++ << ": ";
		if(~ans) {
			cout << ans << '\n';
		}
		else {
			cout << "IMPOSSIBLE" << '\n';
		}
	}

	return 0;
}

