#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>

using namespace std;

void precalc() {

}

void solve() {
	string s;
	cin >> s;

	reverse(s.begin(), s.end());

	for (int i = 0; i + 1 < s.size(); ++i) {
		if (s[i] < s[i + 1]) {
			for (int j = 0; j <= i; ++j) {
				s[j] = '9';
			}
			--s[i + 1];
		}
	}

	while (!s.empty() && s.back() == '0') {
		s.pop_back();
	}

	reverse(s.begin(), s.end());

	cout << s << endl;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	precalc();

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		cout << "Case #" << test << ": ";
		cerr << test << endl;
		solve();
	}
	return 0;
}
