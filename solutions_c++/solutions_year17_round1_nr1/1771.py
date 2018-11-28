#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int main() {
	int numCases;
	ifstream fin("A-large.in");
	ofstream fout("A.out");
	fin >> numCases;
	for (int cases = 1; cases < numCases+1; cases++) {
		int r,c;
		fin >> r >> c;
		char cake[r][c];
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				fin >> cake[i][j];
			}
		}
		set<char> initials;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (cake[i][j] == '?' || initials.count(cake[i][j])) continue;
				initials.insert(cake[i][j]);
				int cstart = j;
				while (cstart > 0) {
					cstart--;
					if (cake[i][cstart] != '?') {
						cstart++;
						break;
					}
					cake[i][cstart] = cake[i][j];
				}
				int cend = j;
				while (cend < c-1) {
					cend++;
					if (cake[i][cend] != '?') {
						cend--;
						break;
					}
					cake[i][cend] = cake[i][j];
				}
				int rstart = i;
				while (rstart > 0) {
					rstart--;
					bool flag = true;
					for (int k = cstart; k <= cend; k++) {
						if (cake[rstart][k] != '?') {
							flag = false;
							break;
						}
					}
					if (flag) {
						for (int k = cstart; k <= cend; k++) {
							cake[rstart][k] = cake[i][j];
						}
					} else {
						rstart++;
						break;
					}
				}
				int rend = i;
				while (rend < r-1) {
					rend++;
					bool flag = true;
					for (int k = cstart; k <= cend; k++) {
						if (cake[rend][k] != '?') {
							flag = false;
							break;
						}
					}
					if (flag) {
						for (int k = cstart; k <= cend; k++) {
							cake[rend][k] = cake[i][j];
						}
					} else {
						rend--;
						break;
					}
				}
			}
		}
		fout << "Case #" << cases << ": " << '\n';
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				fout << cake[i][j];
			}
			fout << '\n';
		}
	}
	return 0;
}
