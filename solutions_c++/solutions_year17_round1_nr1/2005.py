#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void main() {
	int t;

	cin >> t;

	for (int i = 1; i <= t; ++i) {
		int R, C,j;
		string aStr;

		cin >> R >> C;
		vector <vector <char> > aChars(R);
		int k;

		for (j = 0; j < R; ++j) {
			cin >> aStr;

			aChars[j].resize(C);
			for (k = 0; k < C; ++k) {
				aChars[j][k] = aStr[k];
			}

		}

		for (j = 0; j < R; ++j) {
			for (k = 0; k < C; ++k) {
				if (aChars[j][k] == '?') {
					bool isFound = false;
					int ll;

					if (!isFound) {
						for (ll = k - 1; ll >= 0; --ll) {
							if (aChars[j][ll] != '?') {
								isFound = true;
								break;
							}
						}
					}
					if (!isFound) {
						for (ll = k + 1; ll < C; ++ll) {
							if (aChars[j][ll] != '?') {
								isFound = true;
								break;
							}
						}
					}

					if (isFound) {
						aChars[j][k] = aChars[j][ll];
					}
				}
			}
		}

		for (j = 0; j < R; ++j) {
			if (aChars[j][0] == '?') {
				for (k = 0; k < C; ++k) {
					bool isFound = false;
					int ll;

					if (!isFound) {
						for (ll = j - 1; ll >= 0; --ll) {
							if (aChars[ll][k] != '?') {
								isFound = true;
								break;
							}
						}
					}
					if (!isFound) {
						for (ll = j + 1; ll < R; ++ll) {
							if (aChars[ll][k] != '?') {
								isFound = true;
								break;
							}
						}
					}

					if (isFound) {
						aChars[j][k] = aChars[ll][k];
					}
				}
			}
		}

		//cout << n << endl;
		cout << "Case #" << i << ":" << endl;
		for (j = 0; j < R; ++j) {
			for (k = 0; k < C; ++k) {
				cout << aChars[j][k];
			}
			cout << endl;
		}
	}
}
