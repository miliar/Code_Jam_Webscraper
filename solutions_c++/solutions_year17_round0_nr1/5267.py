#include <iostream>
#include <string>

using namespace std;

void single_flip(string& s, int i) {
	s[i] = s[i] == '+' ? '-' : '+';
}

void flip(string& s, int k, int start) {
	for (int i = start; i-start < k && i < s.size(); ++i)
		single_flip(s, i);
}

bool happy(const string& s) {
	for (auto c : s)
		if (c == '-')
			return false;
	return true;
}

int main() {
	string s;
	int T, k, number_flips;

	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin >> s >> k;
		number_flips = 0;
		for (int i = 0; i <= s.size()-k; ++i)
			if (s[i] == '-') {
				flip(s, k, i);
				number_flips++;
			}
		cout << "Case #" << t << ": ";
		if (happy(s))
			cout << number_flips;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}
	
	return 0;
}