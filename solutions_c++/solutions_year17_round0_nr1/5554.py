#include <bits/stdc++.h>

using namespace std;

int t, n, k, l, r, h;
string s;
map <string, int> mp, bp;

char change(char c) { return c == '+' ? '-' : '+'; }

void go(string st) {
	int p = 0;
	string lks = st;
	bp[st] = true, mp[st] = 0;
	for (int i = 0; i < n; i++)
		if (st[i] == '+')
			p++;
	if (p == n) {
		mp[st] = 1;
		return;
	}
	for (int i = 0; i <= n - k; i++) {
		for (int j = i; j < i + k; j++)
			st[j] = change(st[j]);
		if (!bp[st]) go(st);
		if (mp[st] != 0) {
			if (mp[lks] == 0) mp[lks] = mp[st] + 1;
			else mp[lks] = min(mp[lks], mp[st] + 1);
		}
		for (int j = i; j < i + k; j++)
			st[j] = change(st[j]);
	}
}

int main() {
	cin >> t;
	while (t--) {
		cin >> s >> k;
		cout << "Case #" << ++h << ": ";
		mp.clear(), bp.clear(), n = s.size();
		for (int i = 0; i < n; i++)
			if (s[i] == '+')
				l++;
		go(s);
		!mp[s] ? cout << "IMPOSSIBLE\n" : cout << mp[s] - 1 << endl;
	}
	return 0;
}
