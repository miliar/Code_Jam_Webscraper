/*
 * GCJ2017_A1_A.cpp
 *
 *  Created on: Apr 14, 2017
 *      Author: davidzhu
 */

#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;
const int MAXR = 26;

int T, R, C;
char cake[MAXR][MAXR];
bool seen[27];

void expand(int r, int c) {
	int top = r, down = r;
	for(int i = r; i >= 0; i--) {
		if(cake[i][c] == '?' || i == r) {
			cake[i][c] = cake[r][c];
			top = i;
		} else {
			break;
		}
	}
	for(int i = r; i < R; i++) {
		if(cake[i][c] == '?' || i == r) {
			cake[i][c] = cake[r][c];
			down = i;
		} else {
			break;
		}
	}

	for(int i = c-1; i >= 0; i--) {
		bool ok = true;
		for(int j = top; j <= down; j++) {
			if(cake[j][i] != '?') {
				ok = false;
				break;
			}
		}
		if(!ok) break;
		for(int j = top; j <= down; j++) {
			cake[j][i] = cake[r][c];
		}
	}
	for(int i = c+1; i < C; i++) {
		bool ok = true;
		for(int j = top; j <= down; j++) {
			if(cake[j][i] != '?') {
				ok = false;
				break;
			}
		}
		if(!ok) break;
		for(int j = top; j <= down; j++) {
			cake[j][i] = cake[r][c];
		}
	}
}

void solve() {
	cin >> R >> C;
	string s;

	for(int i = 0; i < 26; i++) {
		seen[i] = false;
	}

	for(int i = 0; i < R; i++) {
		cin >> s;
		for(int j = 0; j < C; j++) {
			cake[i][j] = s[j];
		}
	}

	for(int j = 0; j < C; j++) {
		for(int i = 0; i < R; i++) {
			if(cake[i][j] != '?' && !seen[cake[i][j] - 'A']) {
				expand(i, j);
				seen[cake[i][j] - 'A'] = true;
			}
		}
	}

	cout << endl;
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {
			cout << cake[i][j];
		}
		cout << endl;
	}
}

int main() {
	freopen("GCJ2017_A1_A.in", "r", stdin);
	freopen("GCJ2017_A1_A.out", "w", stdout);
	cin >> T;
	for(int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
}
