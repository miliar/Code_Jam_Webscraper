#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t) {
		string s;
		int k;
		cin >> s >> k;

		int n = s.size(), ans = 0;
		for(int i = 0; i + k <= n; ++i) {
			if(s[i] == '+')
				continue;

			++ans;
			int cnt = k;
			for(int j = i; cnt > 0; ++j){
				if(s[j] == '+')
					s[j] = '-';
				else
					s[j] = '+';
				--cnt;
			}

		}
		bool ok = 1;
		for(int i = 0; i < n; ++i) {
			if(s[i] == '-') {
				ok = 0;
				break;
			}
		}

		cout << "Case #" << t <<": ";
		if(!ok)
			cout << "IMPOSSIBLE\n";
		else
			cout << ans << '\n';
	}
	return 0;
}
