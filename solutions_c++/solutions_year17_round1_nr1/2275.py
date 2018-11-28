#include <iostream>

using namespace std;

char cake[50][50];
char mark[50][50];
char objs[1000];

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int r,c;
		cin >> r >> c;
		int count = 0;
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				cin >> cake[j][k];
				mark[j][k] = 0;
			}
		}
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				if (cake[j][k] != '?' && mark[j][k] == 0) {
					int s,e;
					for (s = k; s >= 0 && (cake[j][s] == '?' || s == k); s--);
					for (e = k; e < c && (cake[j][e] == '?' || e == k); e++);
					e--;
					s++;
					for (int m = j; m < r; m++) {
						int f = 1;
						for (int n = s; n <= e; n++) {
							if (cake[m][n] != '?' && cake[m][n] != cake[j][k]) {
								f = 0;
								break;
							}
						}
						if (f) {
							for (int n = s; n <= e; n++) {
								cake[m][n] = cake[j][k];
								mark[m][n] = 1;
							}
						} else {
							break;
						}
					}
					for (int m = j - 1; m >= 0; m--) {
						int f = 1;
						for (int n = s; n <= e; n++) {
							if (cake[m][n] != '?' && cake[m][n] != cake[j][k]) {
								f = 0;
								break;
							}
						}
						if (f) {
							for (int n = s; n <= e; n++) {
								cake[m][n] = cake[j][k];
								mark[m][n] = 1;
							}
						} else {
							break;
						}
					}

				}
			}
		}
		cout << "Case #" << i+1 << ":\n";
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				cout << cake[j][k];
			}
			cout << endl;
		}
	}
	return 0;
}
