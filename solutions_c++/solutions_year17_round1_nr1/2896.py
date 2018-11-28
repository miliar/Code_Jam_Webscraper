#include<iostream>
#include<string>
using namespace std;
#define MAX 25

int findCharInRow(char c[][MAX], int row,int col) {
	for (int i = 0; i < col; i++) {
		if (c[row][i] >= 'A' && c[row][i] <= 'Z') {
			return i;
		}
	}
	return -1;
}

int findCharInCol(char c[][MAX], int row, int col) {
	for (int i = 0; i < row; i++) {
		if (c[col][i] >= 'A' && c[col][i] <= 'Z') {
			return i;
		}
	}
	return -1;
}

int main() {
	int t,r,c;
	string s;
	char cc[MAX][MAX];
	cin >> t;
	int temp = 1;
	while (t--) {
		cin >> r >> c;

		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				char temp;
				cin >> temp;
				cc[i][j] = temp;
			}
		}

		cout << "Case #" << temp++<< ":"<<endl;
		for (int i = 0; i < r; i++) {
			for (int k = 0; k < c; k++) {
				if (cc[i][k] == '?')
					continue;
				else {
					char rep = cc[i][k];
					for (int l = k-1; l >= 0 && cc[i][l] == '?'; l--) {
						cc[i][l] = rep;
					}
					for (int l = k + 1; l < c && cc[i][l] == '?'; l++) {
						cc[i][l] = rep;
					}
				}
			}
		}

		for (int i = 0; i < c; i++) {
			for (int j = 0; j < r; j++) {
				if (cc[j][i] == '?')
					continue;
				else {
					char rep = cc[j][i];
					for (int k = j - 1;  k >= 0 && cc[k][i] == '?'; k--) {
						cc[k][i] = rep;
					}
					for (int k = j + 1; j < r && cc[k][i] == '?'; k++) {
						cc[k][i] = rep;
					}
				}
			}
		}
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cout << cc[i][j];
			}
			cout << endl;
		}

	}
	char ch;
	return 0;
}
