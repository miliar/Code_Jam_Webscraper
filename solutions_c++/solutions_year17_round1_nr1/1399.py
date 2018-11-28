#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <stdio.h>
#include <string.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	int t;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		int r, c;
		cin >> r >> c;
		char g[26][26];
		for (int i = 0; i < r; i++) {
			cin >> g[i];
		}
		for (int i = 1; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (g[i][j] == '?' && g[i - 1][j] != '?') {
					g[i][j] = g[i - 1][j];
				}
			}
		}
		for (int i = r - 2; i >= 0; i--) {
			for (int j = 0; j < c; j++) {
				if (g[i][j] == '?' && g[i + 1][j] != '?') {
					g[i][j] = g[i + 1][j];
				}
			}
		}
		for (int i = 1; i < c; i++) {
			for (int j = 0; j < r; j++) {
				if (g[j][i] == '?' && g[j][i - 1] != '?') {
					g[j][i] = g[j][i - 1];
				}
			}
		}
		for (int i = c - 2; i >= 0; i--) {
			for (int j = 0; j < r; j++) {
				if (g[j][i] == '?' && g[j][i + 1] != '?') {
					g[j][i] = g[j][i + 1];
				}
			}
		}

		cout << "Case #" << i << ": " << endl;	

		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cout << g[i][j];
			}
			cout << endl;
		}
	
	}
}