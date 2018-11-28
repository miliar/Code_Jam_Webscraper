#include <algorithm>
#include <climits>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <string.h>
#include <vector>
using namespace std;

int rows, cols;
string a[25];

int r1['Z' + 1], r2['Z' + 1], c1['Z' + 1], c2['Z' + 1];

bool emptyRow(int i, int c1, int c2) {
	if (i < 0 || i >= rows)
		return false;
	for (int j = c1; j <= c2; j++)
		if (a[i][j] != '?')
			return false;
	return true;
}

bool emptyCol(int j, int r1, int r2) {
	if (j < 0 || j >= cols)
		return false;
	for (int i = r1; i <= r2; i++)
		if (a[i][j] != '?')
			return false;
	return true;
}

void fillRow(int i, int c1, int c2, char ch) {
	for (int j = c1; j <= c2; j++)
		a[i][j] = ch;
}

void fillCol(int j, int r1, int r2, char ch) {
	for (int i = r1; i <= r2; i++)
		a[i][j] = ch;
}

int main() {
	int cases;
	cin >> cases;
	for (int case_counter = 1; case_counter <= cases; case_counter++) {

		cin >> rows >> cols;
		for (int i = 0; i < rows; i++)
			cin >> a[i];

		memset(r1, 127, sizeof(r1));
		memset(c1, 127, sizeof(c1));
		memset(r2, 255, sizeof(r2));
		memset(c2, 255, sizeof(c2));

		char letter[26];
		int letters = 0;

		for (int i = 0; i < rows; i++)
			for (int j = 0; j < cols; j++)
				if (a[i][j] != '?') {
					char ch = a[i][j];
					if (r2[ch] < 0)
						letter[letters++] = ch;
					if (i < r1[ch])
						r1[ch] = i;
					if (i > r2[ch])
						r2[ch] = i;
					if (j < c1[ch])
						c1[ch] = j;
					if (j > c2[ch])
						c2[ch] = j;
				}

		for (int z = 0; z < letters; z++) {
			char ch = letter[z];
			for (int i = r1[ch]; i <= r2[ch]; i++)
				for (int j = c1[ch]; j <= c2[ch]; j++)
					a[i][j] = ch;
		}

		for (int z = 0; z < letters; z++) {
			char ch = letter[z];
			while (emptyRow(r1[ch] - 1, c1[ch], c2[ch])) {
				fillRow(r1[ch] - 1, c1[ch], c2[ch], ch);
				r1[ch]--;
			}
		}
		for (int z = 0; z < letters; z++) {
			char ch = letter[z];
			while (emptyCol(c1[ch] - 1, r1[ch], r2[ch])) {
				fillCol(c1[ch] - 1, r1[ch], r2[ch], ch);
				c1[ch]--;
			}
		}
		for (int z = 0; z < letters; z++) {
			char ch = letter[z];
			while (emptyRow(r2[ch] + 1, c1[ch], c2[ch])) {
				fillRow(r2[ch] + 1, c1[ch], c2[ch], ch);
				r2[ch]++;
			}
		}
		for (int z = 0; z < letters; z++) {
			char ch = letter[z];
			while (emptyCol(c2[ch] + 1, r1[ch], r2[ch])) {
				fillCol(c2[ch] + 1, r1[ch], r2[ch], ch);
				c2[ch]++;
			}
		}

		cout << "Case #" << case_counter << ":" << endl;
		for (int i = 0; i < rows; i++)
			cout << a[i] << endl;
	}
	return 0;
}
