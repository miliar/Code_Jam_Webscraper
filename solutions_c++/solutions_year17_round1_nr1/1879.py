/*
 * A.cpp
 *
 *  Created on: Apr 14, 2017
 *      Author: sbenw
 */
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int R, C;
		cin >> R >> C;
		char ** cake = new char*[R];
		cout << "Case #" << t + 1 << ":" << endl;
		for (int r = 0; r < R; r++) {
			cake[r] = new char[C];
			cin >> cake[r];
			for (int c = 1; c < C; c++) {
				if (cake[r][c] == '?') {
					cake[r][c] = cake[r][c-1];
				}
			}
			for (int c = C-2; c >= 0; c--) {
				if (cake[r][c] == '?') {
					cake[r][c] = cake[r][c+1];
				}
			}
		}
		for (int r = R-2; r >= 0; r--) {
			if (cake[r][0] == '?') {
				cake[r] = cake[r+1];
			}
		}
		for (int r = 0; r < R; r++) {
			if (cake[r][0] == '?') {
				cake[r] = cake[r-1];
			}
			cout << cake[r] << endl;
		}
		for (int r = 0; r < R; r++) {
			delete [] cake[r];
			cake[r]=NULL;
		}
		delete [] cake;
		cake = NULL;
	}
}


