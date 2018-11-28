#include <bits/stdc++.h>
using namespace std;

void solve(int test) {
	cout << "Case #" << test << ": ";
	string s;
	int k;
	cin >> s >> k;
	int n = s.length();
	int res = 0;
	for (int i = 0; i < n; ++i) {
		if (s[i] == '-') {
			if (i + k - 1 < n) {
				for (int j = i; j <= i + k - 1; ++j) {
					if (s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
				res++;
			} else {
				cout << "IMPOSSIBLE\n";
				return;
			}
		}
	}
	cout << res << "\n";
}

int main()
{
#ifdef LOCAL
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
}









