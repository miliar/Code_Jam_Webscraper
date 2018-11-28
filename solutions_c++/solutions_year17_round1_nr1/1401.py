#include<iostream>

using namespace std;

int main() {
	int t = 0;
	cin >> t;
	for (int p = 1; p <= t; p++) {
		int r, c;
		cin >> r >> c;
		char arr[r][c];
		int b[r][c];
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				char c;
				cin >> c;
				arr[i][j] = c;
				if (c != '?') b[i][j] = 1;
				else b[i][j] = 0;
			}
		}
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				if (b[i][j] == 1) {
					int lft = j - 1;
					while ((lft >= 0) && (arr[i][lft] == '?')) {
						arr[i][lft] = arr[i][j];
						lft--;
					}
					int rht = j + 1;
					while ((rht < c) && (arr[i][rht] == '?')) {
						arr[i][rht] = arr[i][j];
						rht++;
					}
					lft++;
					rht--;
					int up = i - 1;
					int down = i + 1;
					bool done = false;
					while ((up >= 0) && (! done)) {
						int k = lft;
						while ((! done) && (k <= rht)) {
							if (arr[up][k] != '?') done = true;
							k++;
						}
						if (! done) {
							for (int t = lft; t <= rht; t++) arr[up][t] = arr[i][j];
							up--;
						}
					}
					done = false;
					while ((down < r) && (! done)) {
						int k = lft;
						while ((! done) && (k <= rht)) {
							if (arr[down][k] != '?') done = true;
							k++;
						}
						if (! done) {
							for (int t = lft; t <= rht; t++) arr[down][t] = arr[i][j];
							down++;
						}
					}
				}
			}
		}
		cout << "Case #" << p << ":" << endl;
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				cout << arr[i][j];
			}
			cout << endl;
		}
	}
}
