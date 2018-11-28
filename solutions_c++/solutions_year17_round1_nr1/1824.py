#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <climits>
#include <vector>
#include <string>
#include <fstream>
#include <queue>
using namespace std;

int T, R, C;
char cake[30][30];
int flag;

void solve() {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (cake[i][j] == '?') {
				if (j - 1 >= 0 && cake[i][j - 1] != '?') cake[i][j] = cake[i][j - 1];
			}
		}
	}
	for (int i = R - 1; i >= 0; i--) {
		for (int j = C - 1; j >= 0; j--) {
			if (cake[i][j] == '?') {
				if (j + 1 < C && cake[i][j + 1] != '?') cake[i][j] = cake[i][j + 1];
			}
		}
	}
	for (int i = 0; i < R; i++) {
		if (i >= 1 && cake[i][0] == '?' && cake[i - 1][0] != '?') {
			for (int j = 0; j < C; j++) {
				cake[i][j] = cake[i - 1][j];
			}
		}
	}
	for (int i = R - 1; i >= 0; i--) {
		if (i + 1 < R && cake[i][0] == '?' && cake[i + 1][0] != '?') {
			for (int j = 0; j < C; j++) {
				cake[i][j] = cake[i + 1][j];
			}
		}
	}
}

int main() {
	ifstream cin("A-large.in");
	ofstream cout("output.txt");
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> R >> C;
		int cc = 0;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				cin >> cake[i][j];
				if (cake[i][j] == '?') {
					cc++;
				}
			}
		}
		if (cc != 0) {
			solve();
		}
		cout << "Case #" << t << ":" << endl;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				cout << cake[i][j];
			}
			cout << endl;
		}
	}

	return 0;
}