#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cassert>
#include <iomanip>
#include <algorithm>
using namespace std;

using ll = long long int;
ifstream fin("1.in");
ofstream fout("1.out");

char a[25][25];

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		fout << "Case #" << t << ":" << endl;
		int r, c;
		fin >> r >> c;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++ )
				fin >> a[i][j];
			for (int j = 1; j < c; j++)
				if (a[i][j] == '?')
					a[i][j] = a[i][j - 1];
			for (int j = c-2; j >= 0; j--)
				if (a[i][j] == '?')
					a[i][j] = a[i][j + 1];
		}
		for (int i = 1; i<r; i++)
			if (a[i][0] == '?')
				for (int j = 0; j < c; j++)
					a[i][j] = a[i - 1][j];
		for (int i = r - 2; i >= 0; i--)
			if (a[i][0] == '?')
				for (int j = 0; j < c; j++)
					a[i][j] = a[i + 1][j];
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++)
				fout << a[i][j];
			fout << endl;
		}
	}
}
