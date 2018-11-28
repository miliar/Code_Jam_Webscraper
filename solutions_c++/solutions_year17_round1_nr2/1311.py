#define _CRT_SECURE_NO_WARNINGS


#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <unordered_map> //C++11
using namespace std;

typedef long long ll;

int t, n, p;
int r[51];
int q[51][51];
bool ch[51][51];
int board[51][1000001], nex[51][1000001];
int sum;

int main() {
	cin >> t;
	for (int i = 1; i <= t; i++) {
		for (int j = 0; j < 51; j++) {
			for (int k = 0; k < 1000001; k++) {
				board[j][k] = 0;
				nex[j][k] = 0;
			}
		}
		sum = 0;
		cin >> n >> p;
		for (int j = 0; j < n; j++) {
			cin >> r[j];
		}
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < p; k++) {
				cin >> q[j][k];
				ch[j][k] = true;
			}
			sort(q[j], q[j] + p);
		}

		for (int j = 0; j < n; j++) {
			for (int m = 1; ; m++) {
				if (m*r[j] * 0.9 > q[j][p - 1]) break;
				for (int k = 0; k < p; k++) {
					if (m*r[j] * 0.9 <= q[j][k] && q[j][k] <= m*r[j] * 1.1) {
						board[j][m] += 1;
						if (ch[j][k]) ch[j][k] = false;
						else nex[j][m - 1] += 1;
					}
				}
			}
		}
		int min;
		for (int k = 1; k < 1000001; k++) {
			min = 100000;
			for (int j = 0; j < n; j++) {
				if (min > board[j][k]) min = board[j][k];
			}
			sum += min;
			if (k < 1000000) {
				for (int j = 0; j < n; j++) {
					board[j][k + 1] -= max(0, nex[j][k] - board[j][k] + min);
				}
			}
		}
		cout << "Case #" << i << ": " << sum << endl;
	}
}

/*
int t, r, c;
char board[25][25];
char now;

int main() {
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> r >> c;
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				cin >> board[j][k];
			}
		}
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				if (board[j][k] != '?') {
					for (int l = j + 1; l < r; l++) {
						if (board[l][k] != '?') break;
						board[l][k] = board[j][k];
					}
					for (int l = k + 1; l < c; l++) {
						if (board[j][l] != '?') break;
						board[j][l] = board[j][k];
					}
				}
			}
		}
		for (int j = r - 1; j >= 0; j--) {
			for (int k = c - 1; k >= 0; k--) {
				if (board[j][k] != '?') {
					for (int l = j - 1; l >= 0; l--) {
						if (board[l][k] != '?') break;
						board[l][k] = board[j][k];
					}
					for (int l = k - 1; l >= 0; l--) {
						if (board[j][l] != '?') break;
						board[j][l] = board[j][k];
					}
				}
			}
		}
		cout << "Case #" << i << ":" << endl;
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				cout << board[j][k];
			}
			cout << endl;
		}
	}
}
*/