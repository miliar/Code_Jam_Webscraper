#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

inline char rev(char x) {
	return x == '+' ? '-' : '+';
}

void solve() {
	string s;
	int k, res = 0;
	cin >> s >> k;
	for (int i = 0; i <= s.length()-k; ++i) {
		if (s[i] != '+') {
			for (int j = i; j < i+k; j++) s[j] = rev(s[j]);
			res++;
		}
	}
	for (int i = 0; i < s.length(); i++)
		if (s[i] == '-') {
			puts("IMPOSSIBLE");
			return;
		}
		cout << res << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		cout << "Case #" << tt << ": "; 
		solve();
	}

	return 0;
}

