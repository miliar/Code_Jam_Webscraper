#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

char cake[30][30];
bool check[30];

int main() {
	int T, r, c;
	cin >> T;
	for (int i = 0; i < T; i++) {
		string input;
		cin >> r >> c;
		for (int j = 0; j < r; j++) check[j] = false;
		for (int j = 0; j < r; j++) {
			cin >> input;
			for (int k = 0; k < c; k++) {
				cake[j][k] = input[k];
				if (input[k] != '?') check[j] = true;
			}
		}
		for (int j = 0; j < r; j++) {
			if (check[j]) {
				char recent = 'A';
				for (int k = 0; k < c; k++) {
					if (cake[j][k] != '?') {
						recent = cake[j][k];
						break;
					}
				}
				for (int k = 0; k < c; k++) {
					if (cake[j][k] == '?') cake[j][k] = recent;
					else recent = cake[j][k];
				}
			}
		}
		
		int recent = 0;
		for (int j = 0; j < r; j++) {
			if (check[j]) {
				recent = j;
				break;
			}
		}

		for (int j = 0; j < r; j++) {
			if (!check[j]) {
				for (int k = 0; k < c; k++) {
					cake[j][k] = cake[recent][k];
				}
			}
			else {
				recent = j;
			}
		}

		cout << "Case #" << i + 1 << ":" << endl;
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				cout << cake[j][k];
			}
			cout << endl;
		}
	}
}