#include <algorithm>
#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <vector> 

#include <boost\config.hpp>

using namespace std;

typedef unsigned long long ull;  // 18*10^18

void main() {
	string file = "A-small-attempt1";
	ifstream ifile(file + ".in");
	ofstream ofile(file + ".out");
	//
	int T;
	ifile >> T;
	for (int t = 1; t <= T; t++) {
		cout << "t: " << t << endl;
		int R, C;
		ifile >> R >> C;
		vector<string> grid;
		for (int i = 0; i < R; i++) {
			string row;
			ifile >> row;
			grid.push_back(row);
		}
		// rows
		for (int i = 0; i < R; i++) {
			string row = grid[i];
			int prev = -1;
			for (int j = 0; j < C; j++) {
				if (row[j] == '?') continue;
				fill(row.begin() + (prev+1), row.begin()+j, row[j]);
				prev = j;				
			}
			if (prev != -1)
				fill(row.begin() + (prev + 1), row.end(), row[prev]);
			grid[i] = row;
		}
		// columns
		for (int i = 0; i < R; i++) {
			string row = grid[i];
			if (row[0] == '?') {
				int o = i - 1;
				if (i == 0) o = i + 1;
				grid[i] = grid[o];
			}
		}
		//
		ofile << "Case #" << t << ": " << endl;
		for (int i = 0; i < R; i++) {
			ofile << grid[i] << endl;
		}
	}
	//
	ifile.close();
	ofile.close();
}