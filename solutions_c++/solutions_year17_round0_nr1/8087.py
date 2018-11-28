#include <iostream>
#include <string>

using namespace std;

void change(string& s, int pos, int k) {
	for (int i = pos; i < pos + k; ++i) {
		if (s[i] == '+') {
			s[i] = '-';
		}
		else {
			s[i] = '+';
		}
	}
}


int main() {
	int t, k, changes;
	string s;
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		cin >> s >> k;
		changes = 0;
		
		int len = s.length();
		for (int j = 0; j < len; ++j) {
			if (s[j] == '-') {
				if ((j + k) > s.length()) {
					cout << "Case #" << i << ": IMPOSSIBLE" << endl;
					break;
				}
				else {
					change(s, j, k);
					++changes;
				}
			}
			
			if (j == len - 1) {
				cout << "Case #" << i << ": " << changes << endl;
			}
		}
	}
	return 0;
}
