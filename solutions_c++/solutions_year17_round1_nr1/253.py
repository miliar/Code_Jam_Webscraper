#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <queue>
#include <map>

using namespace std;



int main() {
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt ++) {
		cout << "Case #" << tt << ": ";
		char s[25][25];
		int r, c;
		cin >> r >> c;
		for (int i = 0; i < r; i ++) {
			string ss;
			cin >> ss;
			for (int j = 0; j < c; j ++) 
				s[i][j] = ss[j];
		}
		int first_row = -1;
		for (int i = 0; i < r; i ++) {
			for (int j = 0; j < c; j ++) {
				if (s[i][j] != '?') {
					first_row = i;
					break;
				}
			}
			if (first_row != -1) break;
		}
		for (int i = first_row; i < r; i ++) {
			int has_elem = -1;
			for (int j = 0; j < c; j ++) if (s[i][j] != '?') { has_elem = j; break; }
			if (has_elem == -1) {
				for (int j = 0; j < c; j ++) s[i][j] = s[i-1][j];
			} else {
				for (int j = 0; j <= has_elem; j ++) s[i][j] = s[i][has_elem];
				for (int j = has_elem + 1; j < c; j ++) if (s[i][j] == '?') s[i][j] = s[i][j-1];
			}
		}
		for (int i = first_row - 1; i >= 0; i --) {
			int has_elem = -1;
			for (int j = 0; j < c; j ++) if (s[i][j] != '?') { has_elem = j; break; }
			if (has_elem == -1) {
				for (int j = 0; j < c; j ++) s[i][j] = s[i+1][j];
			} else {
				for (int j = 0; j <= has_elem; j ++) s[i][j] = s[i][has_elem];
				for (int j = has_elem + 1; j < c; j ++) if (s[i][j] == '?') s[i][j] = s[i][j-1];
			}
		}
		cout << endl;
		for (int i = 0; i < r; i ++) {
			for (int j = 0; j < c; j ++) cout << s[i][j];
			cout << endl;
		}

	}
	return 0;
}

