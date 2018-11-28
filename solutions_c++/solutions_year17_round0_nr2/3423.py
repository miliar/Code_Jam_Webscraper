#include <bits/stdc++.h>

#define ll long long

using namespace std;

int n;
string s;

int findBadPos(string s) {
	for (int i = n - 2; i >= 0; --i) {
		if (s[i] > s[i + 1]) {
			return i;
		}
	}
	return -1;
}

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> s;
	n = s.length();
	do {
		int vt = findBadPos(s);
		if (vt == -1)
			break;
		s[vt]--;
		for (int j = vt + 1; j < n; ++j)
			s[j] = '9';
	} while (1);
	ll res;
	stringstream ss;
	ss << s;
	ss >> res;
	cout << res << "\n";
}

int main()
{
#ifdef LOCAL
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
}









