#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int cases; cin >> cases;
	for (int cc = 0; cc < cases; ++cc) {
		cout << "Case #" << cc + 1 << ": ";
		string s; cin >> s;
		int firstUntidy = s.size();
		for (int i = ((int)s.size()) - 2; i >= 0; --i)
		  if (s[i] > s[i + 1])
		    --s[i], firstUntidy = i + 1;
		for (int i = firstUntidy; i < s.size(); ++i)
		  s[i] = '9';
		cout << (s[0] == '0' ? s.substr(1) : s) << "\n";
	}
	return 0;
}
