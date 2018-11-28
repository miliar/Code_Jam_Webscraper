#include <bits/stdc++.h>

using namespace std;

vector<char> ans;

set<int> visited;

void runTestCase(int t) {
	int n, r, o, y, g, b, v;
	cin >> n >> r >> o >> y >> g >> b >> v;

	bool impossible = false;
	if(r > b + y) impossible = true;
	if(b > r + y) impossible = true;
	if(y > b + r) impossible = true;

	cout << "Case #" << t << ": ";

	if(impossible) {
		cout << "IMPOSSIBLE" << endl;
	}
	else {
		char prev = ' ';
		char first;
		for(int i = 0; i < n; i++) {
			if(prev == 'r') {
				if(b > y) {
					prev = 'b';
					b--;
					cout << 'B';
				}
				else if(y > b) {
					prev = 'y';
					y--;
					cout << 'Y';
				}
				else if(first == 'b') {
					prev = 'b';
					b--;
					cout << 'B';
				}
				else {
					prev = 'y';
					y--;
					cout << 'Y';
				}
			}
			else if(prev == 'b') {
				if(r > y) {
					prev = 'r';
					r--;
					cout << 'R';
				}
				else if(y > r) {
					prev = 'y';
					y--;
					cout << 'Y';
				}
				else if(first == 'r') {
					prev = 'r';
					r--;
					cout << 'R';
				}
				else {
					prev = 'y';
					y--;
					cout << 'Y';
				}
			}
			else if(prev == 'y') {
				if(b > r) {
					prev = 'b';
					b--;
					cout << 'B';
				}
				else if(r > b) {
					prev = 'r';
					r--;
					cout << 'R';
				}
				else if(first == 'b') {
					prev = 'b';
					b--;
					cout << 'B';
				}
				else {
					prev = 'r';
					r--;
					cout << 'R';
				}
			}
			else {
				if(r > b && r > y) {
					first = 'r';
					r--;
					cout << 'R';
					prev = 'r';
				}
				else if(b > y) {
					first = 'b';
					b--;
					cout << 'B';
					prev = 'b';
				}
				else {
					first = 'y';
					prev = 'y';
					y--;
					cout << 'Y';
				}
			}
		}
		cout << endl;
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
