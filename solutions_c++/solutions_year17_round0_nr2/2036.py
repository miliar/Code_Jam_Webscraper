#include <iostream>
#include <string>

using namespace std;

#define REP(i, n) for(int i(0); i < (int)(n); i++)
#define FOR(i, a, b) for (int i(a); i <= (int)(b); i++)

bool ok(const string &s) {
	for (int i = 1; i < s.length(); i++)
	if (s[i - 1] > s[i])
		return false;
	return true;
}

void Work(int casen) {
	string s;
	cin >> s;
	int n = (int)s.length();
	while (!ok(s)) {
		for (int i = 0; i + 1 < s.length(); i++)
		if (s[i] > s[i + 1]) {
			s[i]--;
			for (int j = i + 1; j < s.length(); j++)
			s[j] = '9';
			break;
		}
	}
	while (s.length() > 1 && s[0] == '0')
		s = s.substr(1);
	cout << "Case #" << casen << ": " << s << endl;
}

int main() {
	int n;
	cin >> n;
	FOR(i, 1, n) {
		Work(i);
	}
	return 0;
}