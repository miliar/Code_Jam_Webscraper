#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <cstdint>

using namespace std;

void solve(int r, int c, int init, char s[25][25]){
	//fill the rows
	for(int i = 0; i < r; i++) {
		for(int j = 1; j < c; j++) {
			if(s[i][j] == '?') {
				if(s[i][j - 1] != '?') {
					s[i][j] = s[i][j - 1];
				}
			}
		}
	}

	for(int i = 0; i < r; i++) {
		for(int j = c - 2; j >= 0; j--) {
			if(s[i][j] == '?') {
				if(s[i][j + 1] != '?') {
					s[i][j] = s[i][j + 1];
				}
			}
		}
	}

	for(int i = 0; i < r; i++) {
		if(s[i][0] == '?') {
			int x = i + 1;
			while(s[x][0] == '?' || x >= r) {
				x++;
				if(x >= r) {
					x = i - 1;
					while(s[x][0] == '?') {
						x--;
					}
					if(x < 0) {
						cerr << "err" << endl;
					}
				}
			}
			for(int j = 0; j < c; j++) {
				s[i][j] = s[x][j];
			}
		}
	}

	for(int i = 0; i < r; i++) {
		for(int j = 0; j < c; j++) {
			cout << s[i][j];
		}
		cout << endl;
	}
	
}

int main() {
	int t, r, c, init;

	cin >> t;

	for(int i = 0; i < t; i++){
		cin >> r;
		cin >> c;

		char s[25][25];
		for(int i = 0; i < 25; i++) {
			for(int j = 0; j < 25; j++) {
				s[i][j] = '?';
			}
		}
		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
				char cur;
				cin >> cur;
				if(cur != '?')
					init++;
				s[i][j] = cur;
			}
		}
		cout << "Case #" << (i + 1) << ":" << endl;
		solve(r, c, init, s);
	}

	return EXIT_SUCCESS;
}
