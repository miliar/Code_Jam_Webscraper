#include <bits/stdc++.h>

using namespace std;

void runTestCase(int t) {
	int r, c;
	cin >> r >> c;

	vector<string> cake(r);
	for(int i = 0; i < r; i++) {
		cin >> cake[i];
	}

	for(int i = 0; i < r; i++) {
		int prev = '?';
		for(int j = 0; j < c; j++) {
			if(cake[i][j] == '?') {
				cake[i][j] = prev;
			}
			else {
				prev = cake[i][j];
			}
		}
		for(int j = c-1; j >= 0; j--) {
			if(cake[i][j] == '?') {
				cake[i][j] = prev;
			}
			else {
				prev = cake[i][j];
			}
		}
	}

	for(int i = 0; i < c; i++) {
		int prev = '?';
		for(int j = 0; j < r; j++) {
			if(cake[j][i] == '?') {
				cake[j][i] = prev;
			}
			else {
				prev = cake[j][i];
			}
		}
		for(int j = r-1; j >= 0; j--) {
			if(cake[j][i] == '?') {
				cake[j][i] = prev;
			}
			else {
				prev = cake[j][i];
			}
		}
	}

	cout << "Case #" << t << ": ";
	cout << endl;
	for(int i = 0; i < r; i++) {
		cout << cake[i] << endl;
	}
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		runTestCase(i);
	}

	return 0;
}
