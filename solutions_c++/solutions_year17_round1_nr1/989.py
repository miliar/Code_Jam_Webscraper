#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

int main() {
	ofstream fout("cake.out");
	ifstream fin("cake.in");
	int T;
	fin >> T;
	for (int t = 0; t<T; t++) {
		int R, C;
		fin >> R >> C;
		int xMax[30];
		int xMin[30];
		int yMax[30];
		int yMin[30];
		bool ex[30];
		char cake[30][30];
		for (int i = 0; i < 26; i++) {
			ex[i] = false;
			xMax[i] = -1;
			xMin[i] = 30;
			yMax[i] = -1;
			yMin[i] = 30;
		}
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				char temp;
				fin >> temp;
				cake[r][c] = temp;
				int in = temp - 65;
				ex[in] = true;
				xMax[in] = max(xMax[in], r);
				yMax[in] = max(yMax[in], c);
				xMin[in] = min(xMin[in], r);
				yMin[in] = min(yMin[in], c);
				cout << temp;
			}
			cout << endl;
		}
		for (int i = 0; i < 26; i++) {
			if (ex[i]) {
				for (int r = xMin[i]; r < xMax[i] + 1; r++) {
					for (int c = yMin[i]; c < yMax[i] + 1; c++) {
						cake[r][c] = i + 65;
					}
				}
			}
		}
		for (int i = 0; i < 26; i++) {
			if (ex[i]) {
				bool up = true;
				bool down = true;
				bool left = true;
				bool right = true;
				while (up || down || left || right) {
					for (int k = xMin[i]; (k < xMax[i] + 1); k++) {
						if (yMin[i] > 0) {
							if (cake[k][yMin[i] - 1] != '?') down = false;
						}
						else down = false;
						if (yMax[i] < C-1) {
							if (cake[k][yMax[i] + 1] != '?') up = false;
						}
						else up = false;
					}
					if (down) {
						for (int k = xMin[i]; (k < xMax[i] + 1); k++) {
							cake[k][yMin[i] - 1] = i + 65;
						}
						yMin[i]--;
						left = true;
						right = true;
					}
					if (up) {
						for (int k = xMin[i]; (k < xMax[i] + 1); k++) {
							cake[k][yMax[i] + 1] = i + 65;
						}
						yMax[i]++;
						left = true;
						right = true;
					}
					for (int k = yMin[i]; (k < yMax[i] + 1); k++) {
						if (xMin[i] > 0) {
							if (cake[xMin[i]-1][k] != '?') left = false;
						}
						else left = false;
						if (xMax[i] < R - 1) {
							if (cake[xMax[i]+1][k] != '?') right = false;
						}
						else right = false;
					}
					if (right) {
						for (int k = yMin[i]; k < yMax[i] + 1; k++) {
							cake[xMax[i]+1][k] = i + 65;
						}
						xMax[i]++;
						up = true;
						down = true;
					}
					if (left) {
						for (int k = yMin[i]; k < yMax[i] + 1; k++) {
							cake[xMin[i]-1][k] = i + 65;
						}
						xMin[i]--;
						up = true;
						down = true;
					}
				}
				for (int r = 0; r < R; r++) {
					for (int c = 0; c < C; c++) {
						cout << cake[r][c];
					}
					cout << endl;
				}
			}
		}
		fout << "Case #" << t + 1 << ":" << endl;
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				fout << cake[r][c];
			}
			fout << endl;
		}
	}
	system("pause");
}