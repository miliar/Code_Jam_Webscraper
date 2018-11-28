// CodeJam.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main()
{
	int t, r, c;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> r >> c;
		char sets[25][25];

		for (int j = 0; j < r; ++j)
			for (int k = 0; k < c; ++k)
				cin >> sets[j][k];

		for (int j = 0; j < r; ++j)
			for (int k = 0; k < c; ++k) {
				if (sets[j][k] != '?') {
					char used = sets[j][k];
					for (int y = k - 1; y >= 0; y--) {
						if (sets[j][y] != '?') {
							break;
						}
						else {
							sets[j][y] = used;
						}
					}
					for (int y = k + 1; y < c; y++) {
						if (sets[j][y] != '?') {
							k = y - 1;
							break;
						}
						else {
							sets[j][y] = used;
						}
					}
				}
			}

		for (int j = 0; j < r; ++j) {
			if (sets[j][0] != '?') {
				for (int y = j - 1; y >= 0; y--) {
					if (sets[y][0] != '?')
						break;
					for (int k = 0; k < c; ++k) {
						sets[y][k] = sets[j][k];
					}
				}

				for (int y = j + 1; y < r; y++) {
					if (sets[y][0] != '?')
						break;
					for (int k = 0; k < c; ++k) {
						sets[y][k] = sets[j][k];
					}
				}
			}
		}

		cout << "Case #" << i << ": " << endl;
		for (int j = 0; j < r; ++j) {
			for (int k = 0; k < c; ++k) {
				cout << sets[j][k];
			}
			cout << endl;
		}

	}
	//cin >> t;
	return 0;
}