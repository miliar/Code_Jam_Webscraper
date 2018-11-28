#include <iostream>
using namespace std;

long solve(string s) {
	if (s.size() == 1) {
		return s[0] - '0';
	}
	bool tidy = true;
	int d, i, L, last;
	long a = 0;
	for (i = 0, L = s.size(); i < L; ++i) {
		d = s[i] - '0';
		a = a * 10 + d;
		if (i == 0) continue;
		if (s[i] < s[i - 1]) {
			tidy = false;
			a /= 10;
			break;
		}
	}
	if (tidy) return a;
	for (i -= 1; i >= 0; --i) {
		a -= 1;
		if (a % 10 && (a % 10 >= (a / 10) % 10)) {
			break;
		}
		a /= 10;
	}
	if (!a) i += 1;
	for (i += 1; i < L; ++i) {
		a = a * 10 + 9;
	}
	return a;
}

int main() {
	int T, t;
	string s;
	cin >> T;
	for (t = 1; t <= T; ++t) {
		cin >> s;
		cout << "Case #" << t << ": " << solve(s) << endl;
	}
	return 0;
}
