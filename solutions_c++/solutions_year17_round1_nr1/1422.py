// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

char cake[30][30];
char firsts[30];
int T;
int R;
int C;

int main()
{
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cin >> R;
		cin >> C;

		for (int j = 0; j < R; j++) {
			cin >> cake[j];
			firsts[j] = '?';
		}

		for (int j = 0; j < R; j++) {
			for (int k = 0; k < C; k++) {
				if (cake[j][k] != '?') {
					firsts[j] = cake[j][k];
					break;
				}
			}
		}

		for (int j = 0; j < R; j++) {
			for (int k = 0; k < C; k++) {
				if (firsts[j] != '?') {
					if (cake[j][k] == '?') {
						if (k == 0) {
							cake[j][k] = firsts[j];
						}
						else {
							cake[j][k] = cake[j][k - 1];
						}
					}
				}
				else if (j != 0) {
					cake[j][k] = cake[j - 1][k];
				}
			}
		}

		for (int j = R-1; j >= 0; j--) {
			for (int k = C-1; k >= 0; k--) {
				if (cake[j][k] == '?') {
					cake[j][k] = cake[j+1][k];
				}
			}
		}



		cout << "Case #" << i << ":" << endl;
		for (int j = 0; j < R; j++) {
			for (int k = 0; k < C; k++) {
				cout << cake[j][k];
			}
			cout << endl;
		}
	}

	return 0;
}

