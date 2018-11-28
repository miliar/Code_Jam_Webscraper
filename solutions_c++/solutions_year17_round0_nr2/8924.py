#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n ; i++) {
		string s;
		cin >> s;
		if (s.size() == 1) {
			cout << "Case #" << i + 1 << ": " << s << endl;
			continue;
		}
		int j;
		for (j = 1; j < s.size() && (s[j] >= s[j - 1]); j++);
		if (j == s.size()) {
			cout << "Case #" << i + 1 << ": " << s << endl;
			continue;
		}
		while (j != s.size()) {
			for (int k = j; k < s.size(); k++) {
				s[k] = '9';
			}
			j--;
			while(s[j] == '0') {
				s[j--] = '9';
			}
			s[j]--;
			for (j = 1; j < s.size() && (s[j] >= s[j - 1]); j++);
		}
		if (s[0] == '0') {
			s = s.substr(1, s.size() - 1);
		}
		cout << "Case #" << i + 1 << ": " << s << endl;
	}
}
