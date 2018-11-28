#include <bits/stdc++.h>
using namespace std;

string run() {
	string n; cin >> n;
	string res (n.size(), '0');
	for (int i = 0; i < (int) res.size(); ++i) {
		for (int c = '9'; c >= '0'; --c) {
			fill(res.begin() + i, res.end(), c);
			if (res <= n) break;
		}
	}
	for (int i = 0; i < (int) res.size(); ++i)
		if (res[i] != '0')
			return res.substr(i);
	assert(false);
}

int main() {
	int nt; cin >> nt;
	for (int tc = 1; tc <= nt; ++tc) cout << "Case #" << tc << ": " << run() << '\n';
	return 0;
}
