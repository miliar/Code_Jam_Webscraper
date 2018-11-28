#include <iostream>
#include <vector>
#include <string>

using namespace std;
using i64 = long long;

string solve(string s) {
	int n = s.length();
	for (int i = 1; i < s.length(); ++i)
		if (s[i] < s[i - 1]) {
			--s[i - 1];
			for (int j = i; j < s.length(); ++j)
				s[j] = '9';
			return solve(s);
		}
	return s;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; ++t) {
		string s;
		cin >> s;
		auto ans = solve(s);
		cout << "Case #" << t << ": ";
		bool beg = true;
		for (char c : ans) {
			if (c != '0')
				beg = false;
			if (!beg)
				cout << c;
		}
		cout << endl;
	}
}