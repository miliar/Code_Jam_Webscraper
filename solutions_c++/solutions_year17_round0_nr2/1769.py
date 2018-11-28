#include <iostream>
#include <string>

using namespace std;

void SolveA(string s, int K) {
	int ans = 0;
	for (int i = 0; i < s.length() - K + 1; ++i) {
		if (s[i] == '-') {
			++ans;
			for (int j = i; j < i + K; ++j) {
				s[j] = s[j] == '-' ? '+' : '-';
			}
		}
	}
	if (s.find('-') != string::npos) {
		cout << "IMPOSSIBLE";
		return;
	}

	cout << ans;
}

void SolveB(string s) {
	for (int i = s.length() -1; i > 0; --i) {
		char prev = s[i - 1];
		char curr = s[i];
		if (curr < prev) {
			s[i - 1] = s[i - 1] - 1;
			for (int j = i; j < s.length(); ++j) {
				s[j] = '9';
			}
		}
	}
	cout << s.substr(s.find_first_not_of('0'));
}

void main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		string s;
		cin >> s;
		cout << "Case #" << i + 1 << ": ";
		SolveB(s);
		cout << endl;
	}
}