#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int T, R, C;
char grid [30][30];
bool A [30];
bool B [30];
vector<pair<char, pair<int, int> > > initials;

pair<int, int> check_row (int r, int c) {
	int lo = c;
	int hi = c;
	while (lo-1 >= 0 && grid[r][lo-1] == '?') 
		lo--;
	while (hi+1 < C && grid[r][hi+1] == '?') 
		hi++;
	return make_pair(lo, hi);
}

pair<int, int> check_col (int r, int c) {
	int lo = r;
	int hi = r;
	while (lo-1 >= 0 && grid[lo-1][c] == '?') 
		lo--;
	while (hi+1 < R && grid[hi+1][c] == '?') 
		hi++;
	return make_pair(lo, hi);
}

bool check2 (int lo, int hi, int c) {
	for (int i = lo; i <= hi; i++)
		if (grid[i][c] != '?')
			return false;
	return true;
}

bool check1 (int lo, int hi, int r) {
	for (int i = lo; i <= hi; i++)
		if (grid[r][i] != '?')
			return false;
	return true;
}

void fill(char ch, int b, int a, int d, int c) {
	for (int i = a; i <= c; i++) 
		for (int j = b; j <= d; j++)
			grid[i][j] = ch;
}

int main() {
	ifstream fin ("A.in");
	ofstream fout ("A.out");

	fin >> T;
	for (int t = 1; t <= T; t++) {
		initials.clear();
		for (int i = 0; i < 30; i++) {
			A[i] = false;
			B[i] = false;
			for (int j = 0; j < 30; j++)
				grid[i][j] = '?';
		}
		fout << "Case #" << t << ":" << endl;
		fin >> R >> C;
		string line;
		for (int r = 0; r < R; r++) {
			fin >> line;
			for (int c = 0; c < C; c++) {
				grid[r][c] = line[c];
				if (line[c] != '?') {
					A[r] = true;
					B[c] = true;
					initials.push_back(make_pair(line[c], make_pair(r, c)));
				}
			}
		}
		for (int i = 0; i < initials.size(); i++) {
			char ch = initials[i].first;
			int r = initials[i].second.first;
			int c = initials[i].second.second;

			pair<int, int> p = check_row(r, c);
			if (p.first == p.second) {
				p = check_col(r, c);
				if (p.first != p.second) {
					int x = c;
					int y = c;
					while (x-1 >= 0 && check2(p.first, p.second, x-1))
						x--;
					while (y+1 < C && check2(p.first, p.second, y+1))
						y++;
					fill (ch, x, p.first, y, p.second);
				}
			} else {
				int x = r;
				int y = r;
				while (x-1 >= 0 && check1(p.first, p.second, x-1))
					x--;
				while (y+1 < R && check1(p.first, p.second, y+1))
					y++;
				fill (ch, p.first, x, p.second, y);
			}
		}
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++)
				fout << grid[i][j];
			fout << endl;
		}
	}

	fout.close();

	return 0;
}