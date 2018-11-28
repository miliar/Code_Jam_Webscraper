#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <vector> 
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
//#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <cmath>
//#include <cstdio>
#include <fstream>
using namespace std;

int main()
{
	int T;
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	fin >> T;
	for (int t = 0; t < T; t++) {
		int r, c;
		fin >> r >> c;
		vector<vector<char>> grid(r, vector<char>(c));
		for (auto& row : grid) {
			for (char& c : row)
			{
				fin >> c;
			}
		}

		for (int i = 0; i < r; i++) {
			char p = '?';
			for (int j = 0; j < c; j++) {
				bool not = p == '?';
				if (grid[i][j] != '?') {
					p = grid[i][j];
					if (not) {
						for (int k = 0; k < j; k++)
							grid[i][k] = p;
					}
						
				}
				else {
					if (p != '?')
						grid[i][j] = p;
				}
			}
		}

		int good = -1;
		for (int i = 0; i < r; i++) {
			bool not = good == -1;
			if (grid[i][0] != '?') {
				good = i;
				if (not) {
					for (int k = 0; k < i; k++) {
						for (int m = 0; m < c; m++) {
							grid[k][m] = grid[i][m];
						}
					}
				}
				continue;
			}
			if (good != -1) {
				for (int j = 0; j < c; j++)
					grid[i][j] = grid[good][j];
			}
		}

		fout << "Case #" << t + 1 << ":\n";
		for (auto& row : grid) {
			for (char& c : row)
			{
				fout << c;
			}
			fout << endl;
		}

	}
}