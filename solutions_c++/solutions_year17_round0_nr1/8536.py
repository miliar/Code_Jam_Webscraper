#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("A_in.txt", "r", stdin);
	freopen("A_out.txt", "w", stdout);

	int t; cin >> t;
	for (int i = 0; i < t; i++) {
		string s; 	cin >> s;
		int k;		cin >> k;
		int n = s.size();
		int ans = 0;

		bool up[n];
		for (int i = 0; i < n; i++)
			up[i] = (s[i] == '+');

		for (int i = 0; i <= n - k; i++) {
			if (!up[i]) {
				for (int j = 0; j < k; j++)
					up[i + j] = !up[i + j];
				ans++;
			}
		}

		cout << "Case #" << (i + 1) << ": ";
		bool dead = 0;
		for (int i = 0; i < n && !dead; i++) {
			if (!up[i]) {
				cout << "IMPOSSIBLE" << endl;
				dead = 1;
			}
		}

		if (!dead)
			cout << ans << endl;
	}
}
