#include <bits/stdc++.h>

using namespace std;

int R, C;
char strs[50][50];

int main() {

	int T;
	cin >> T;

	for (int ka = 1; ka <= T; ka++) {
		cin >> R >> C;

		for (int i = 0; i < R; i++) 
			cin >> strs[i];

		for (int i = 0; i < R; i++) {

			char pchar = '?';
			bool empty = true;

			for (int j = 0; j < C; j++) {
				if (strs[i][j] != '?') {
					pchar = strs[i][j];
				}
				else {
					strs[i][j] = pchar;
				}
			}

			for (int j = C-1; j >= 0; j--) {
				if (strs[i][j] != '?') {
					pchar = strs[i][j];
					empty = false;
				}
				else {
					strs[i][j] = pchar;
				}
			}

			if (empty && i != 0) {
				for (int j = 0; j < C; j++) {
					strs[i][j] = strs[i-1][j];
				}
			}

		}

		for (int i = R-1; i >= 0; i--) {

			char pchar = '?';
			bool empty = true;

			for (int j = 0; j < C; j++) {
				if (strs[i][j] != '?') {
					pchar = strs[i][j];
				}
				else {
					strs[i][j] = pchar;
				}
			}

			for (int j = C-1; j >= 0; j--) {
				if (strs[i][j] != '?') {
					pchar = strs[i][j];
					empty = false;
				}
				else {
					strs[i][j] = pchar;
				}
			}

			if (empty && i != R-1) {
				for (int j = 0; j < C; j++) {
					strs[i][j] = strs[i+1][j];
				}
			}

		}

		printf("Case #%d:\n", ka);

		for (int i = 0; i < R; i++) {
			printf("%s\n", strs[i]);
		}


	}


	return 0;
}