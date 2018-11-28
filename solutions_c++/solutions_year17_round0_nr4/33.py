#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <stack>
#include <queue>

using namespace std;



int main() {
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt ++) {
		int n, m;
		cin >> n >> m;
		int star_[100][100];
		int plus_[100][100];
		int star[100][100];
		int plus[100][100];
		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < n; j ++) {
				star[i][j] = star_[i][j] = 0;
				plus[i][j] = plus_[i][j] = 0;
			}
		}
		while (m--) {
			char s;
			int r, c;
			cin >> s >> r >> c;
			r--; c--;
			star[r][c] = star_[r][c] = (s == 'x' || s == 'o');
			plus[r][c] = plus_[r][c] = (s == '+' || s == 'o');
		}
		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < n; j ++) {
				if (star[i][j] == 1) {
					for (int k = 0; k < n; k ++) {
						if (j != k) star[i][k] = 2;
						if (i != k) star[k][j] = 2;
					}
				}
				if (plus[i][j] == 1) {
					for (int ii = i-1, jj = j-1; ii >= 0 && jj >= 0; ii--, jj--) plus[ii][jj] = 2;
					for (int ii = i-1, jj = j+1; ii >= 0 && jj < n; ii--, jj++) plus[ii][jj] = 2;
					for (int ii = i+1, jj = j-1; ii < n && jj >= 0; ii++, jj--) plus[ii][jj] = 2;
					for (int ii = i+1, jj = j+1; ii < n && jj < n; ii++, jj++) plus[ii][jj] = 2;
				}
			}
		}
		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < n; j ++) {
				if (star[i][j] == 0) {
					star[i][j] = 1;
					for (int k = 0; k < n; k ++) {
						if (j != k) star[i][k] = 2;
						if (i != k) star[k][j] = 2;
					}
				}
			}
		}
		for (int kk = 0; kk < 2*n; kk ++) {
			int k;
			if (kk % 2 == 0) k = kk / 2;
			else k = (2*n-1) - kk / 2;
			//for (int j = max(0,k-n+1); j < min(k+1,n); j ++) {
//			cout << k << endl;
			for (int j1 = max(0,k-n+1), j2 = min(k+1,n)-1; j1 <= j2; j1++, j2--) {
				int j = j1, i = k-j;
				if (plus[i][j] == 0) {
					plus[i][j] = 1;
					for (int ii = i-1, jj = j-1; ii >= 0 && jj >= 0; ii--, jj--) plus[ii][jj] = 2;
					for (int ii = i-1, jj = j+1; ii >= 0 && jj < n; ii--, jj++) plus[ii][jj] = 2;
					for (int ii = i+1, jj = j-1; ii < n && jj >= 0; ii++, jj--) plus[ii][jj] = 2;
					for (int ii = i+1, jj = j+1; ii < n && jj < n; ii++, jj++) plus[ii][jj] = 2;
				}
				j = j2; i = k-j;
				if (plus[i][j] == 0) {
					plus[i][j] = 1;
					for (int ii = i-1, jj = j-1; ii >= 0 && jj >= 0; ii--, jj--) plus[ii][jj] = 2;
					for (int ii = i-1, jj = j+1; ii >= 0 && jj < n; ii--, jj++) plus[ii][jj] = 2;
					for (int ii = i+1, jj = j-1; ii < n && jj >= 0; ii++, jj--) plus[ii][jj] = 2;
					for (int ii = i+1, jj = j+1; ii < n && jj < n; ii++, jj++) plus[ii][jj] = 2;
				}
			}
		}
		int y = 0, z = 0;
		vector<pair<char,pair<int,int>>> v;
		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < n; j ++) {
				if (star[i][j] == 1 && plus[i][j] == 1) {
					y += 2;
					if (star_[i][j] == 1 && plus_[i][j] == 1) continue;
					z ++; v.push_back({'o', {i, j}});
				} else if (star[i][j] == 1) {
					y ++;
					if (star_[i][j] == 1) continue;
					z ++; v.push_back({'x', {i, j}});
				} else if (plus[i][j] == 1) {
					y ++;
					if (plus_[i][j] == 1) continue;
					z ++; v.push_back({'+', {i, j}});
				}
			}
		}
		cout << "Case #" << tt << ": ";
		cout << y << ' ' << z << endl;
		for (auto &item : v) {
			cout << item.first << ' ' << item.second.first + 1 << ' ' << item.second.second + 1 << endl;
		}
	}

	return 0;
}

