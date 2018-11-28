#include <iostream>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int testcase, r, c;
	cin >> testcase;
	for (int t = 1; t <= testcase; t++) {
		string s[32];
		cin >> r >> c;
		for (int i = 0; i < r; i++)
			cin >> s[i];
		for (int i = 0; i < r; i++) {
			char pre = '?';
			for (int j = 0; j < c; j++) {
				if (pre == '?') {
					if (pre != s[i][j])
						pre = s[i][j];
				} else {
					if (s[i][j] == '?')
						s[i][j] = pre;
					else
						pre = s[i][j];
				}
			}
		}
		for (int i = 0; i < r; i++) {
			char pre = '?';
			for (int j = c - 1; j > -1; j--) {
				if (pre == '?') {
					if (pre != s[i][j])
						pre = s[i][j];
				} else {
					if (s[i][j] == '?')
						s[i][j] = pre;
					else
						pre = s[i][j];
				}
			}
		}

		for (int j = 0; j < c; j++) {
			char pre = '?';
			for (int i = 0; i < r; i++) {
				if (pre == '?') {
					if (pre != s[i][j])
						pre = s[i][j];
				} else {
					if (s[i][j] == '?')
						s[i][j] = pre;
					else
						pre = s[i][j];
				}
			}
		}

		for (int j = 0; j < c; j++) {
			char pre = '?';
			for (int i = r - 1; i > -1; i--) {
				if (pre == '?') {
					if (pre != s[i][j])
						pre = s[i][j];
				} else {
					if (s[i][j] == '?')
						s[i][j] = pre;
					else
						pre = s[i][j];
				}
			}
		}
		cout << "Case #" << t << ":" <<endl;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++){
				cout << s[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}