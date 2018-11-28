#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cout << "Case #" << t + 1 << ":" << endl;

		int r, c;
		cin >> r >> c;
		char a[25][25];
		for (int i = 0; i < r; i++) {
			string s;
			cin >> s;
			for (int j = 0; j < c; j++) {
				a[i][j] = s[j];
			}
		}
		char h[25];
		for (int i = 0; i < r; i++) {
			h[i] = '?';
			for (int j = 0; j < c; j++) {
				if (a[i][j] != '?') {
					h[i] = a[i][j];
					break;
				}
			}
		}
		for (int i = 0; i < r; i++) {
			if (h[i] != '?') {
				for (int j = 0; j < c; j++) {
					if (a[i][j] == '?') {
						a[i][j] = h[i];
					} else {
						h[i] = a[i][j];
					}
				}
			}
		}
		for (int i = 1; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (a[i][j] == '?') {
					a[i][j] = a[i - 1][j];
				}
			}
		}
		for (int i = r - 2; i >= 0; i--) {
			for (int j = 0; j < c; j++) {
				if (a[i][j] == '?') {
					a[i][j] = a[i + 1][j];
				}
			}
		}
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cout << a[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}
