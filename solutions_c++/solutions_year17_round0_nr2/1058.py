#include <iostream>
#include <string>
#include <sstream>

using namespace std;

void solve() {
	string s;
	cin >> s;
	int p = 0;
	while (p + 1 < s.size() && s[p] <= s[p + 1])
		p++;
	if (p < s.size() - 1) {
		while (p > 0 && s[p - 1] == s[p])
			p--;
		s[p++]--;
		while (p < s.size())
			s[p++] = '9';
	}
	long long res;
	stringstream ss(s);
	ss >> res;
	cout << res << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
