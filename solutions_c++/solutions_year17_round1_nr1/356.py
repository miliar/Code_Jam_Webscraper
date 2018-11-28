#include <iostream>
#include <string>
#include <string.h>
#include <map>
#include <vector>
using namespace std;


char m[30][30];
int f[30][30];

bool fun(int y, int xmin, int xmax) {
	for (int i = xmin; i <= xmax; i ++) {
		if (m[i][y] != '?') return false;
	}
	return true;
}
int main () {
	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ti ++) {
		int r, c;
		cin >> r >> c;
		for (int i = 0; i < r; i ++) {
			for (int j = 0; j < c; j ++) {
				cin >> m[j][i];
				f[j][i] = 0;
			}
		}
		for (int i = 0; i < r; i ++) {
			for (int j = 0; j < c; j ++) {
				if (m[j][i] != '?' && f[j][i] == 0) {
					int xmin = j-1, xmax = j+1;
					while (xmin >= 0 && m[xmin][i] == '?') xmin --;
					while (xmax < c && m[xmax][i] == '?') xmax ++;
					xmin ++; xmax --;
					// cout << xmin << " " << xmax << endl;
					int ymin = i-1, ymax = i+1;
					while (ymin >= 0 && fun(ymin, xmin, xmax)) ymin --;
					while (ymax < r && fun(ymax, xmin, xmax)) ymax ++;
					ymin ++; ymax --;
					// cout << ymin << " " << ymax << endl;
					for (int ii = ymin; ii <= ymax; ii ++) {
						for (int jj = xmin; jj <= xmax; jj ++) {
							m[jj][ii] = m[j][i];
							f[jj][ii] = 1;
						}
					}
				}
			}
		}
		
		// if (ans != -1) {
			cout << "Case #" << ti << ": " << endl;
		for (int i = 0; i < r; i ++) {
			for (int j = 0; j < c; j ++) {
				cout << m[j][i];
			}
			cout << endl;
		}
		// } else {
		// 	cout << "Case #" << ti << ": IMPOSSIBLE" << endl; 
		// }
	}
}