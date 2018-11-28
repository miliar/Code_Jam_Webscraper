#include <iostream>

using namespace std;

int main()
{
	int t, r, c;

	cin >> t;
	for (int i = 1; i <= t; i++) {
		char cake[25][25];
		int dir[25][25];
		cin >> r >> c;
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				cin >> cake[j][k];
			}
		}
		for (int j = 0; j < r; j++) {
			for (int k = 1; k < c; k++) {
				if (cake[j][k] != '?') {
					for (int l = k - 1; l >= 0 && cake[j][l] == '?'; l--) {
						cake[j][l] = cake[j][k];
					}
				}
			}
			for (int k = c - 2; k >= 0; k--) {
				if (cake[j][k] != '?') {
					for (int l = k + 1; l < c && cake[j][l] == '?'; l++) {
						cake[j][l] = cake[j][k];
					}
				}
			}
		}
		for (int k = 0; k < c; k++) {
			for (int j = 1; j < r; j++) {
				if (cake[j][k] != '?') {
					for (int l = j - 1; l >= 0 && cake[l][k] == '?'; l--) {
						cake[l][k] = cake[j][k];
					}
				}
			}
			for (int j = r - 2; j >= 0; j--) {
				if (cake[j][k] != '?') {
					for (int l = j + 1; l < r && cake[l][k] == '?'; l++) {
						cake[l][k] = cake[j][k];
					}
				}
			}
		}
		cout << "Case #" << i << ":\n";
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				cout << cake[j][k];
			}
			cout << endl;
		}
	}
	return 0;
}
