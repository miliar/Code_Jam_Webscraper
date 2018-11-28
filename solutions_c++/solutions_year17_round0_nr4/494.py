#include <vector>
#include <iostream>
#include <sstream>

using namespace std;

template<typename T> ostream& operator<<(ostream& str,             const vector<T>& v) { str << "["; for(auto n : v) str << n << ", "; str << "]"; return str; }


template<typename T>
std::ostream& operator<<(std::ostream& str, const std::vector<std::vector<T>>& vv) {
	for(auto n : vv) {
		str << n << std::endl;
	}
	return str;
}

#define debug(x) cout <<  #x  << ": " << x << endl


int maxscore;
vector<vector<char>> maxboard;


/*
void extend_bishops(int udiag, int count, vector<vector<char>>& grid, vector<bool>& udiagvis, vector<bool>& ddiagvis) {
	int n = grid.size();

	if (count > maxscore) {
		maxscore = count;
		maxboard = grid;
	}

	if (udiag >= 2*n-1) {
		return;
	}

	if (udiagvis.at(udiag)) {
		extend_bishops(udiag+1, count, grid, udiagvis, ddiagvis);
		return;
	}

	int x = max(0, udiag-n);
	int y = max(0, n-udiag-1);
	// int y = 2 - max(0, udiag-n);

	debug(udiag);

	// udiagvis.at(udiag) = true;
	while (x < n && y < n) {
		int ddiag = (n-1) + (x-y);

		debug(x);
		debug(y);
		// debug(ddiag);

		if (!ddiagvis.at(ddiag)) {
			ddiagvis.at(ddiag) = true;
			char c = grid.at(x).at(y);
			grid.at(x).at(y) = '+';
			extend_bishops(udiag+1, count+1, grid, udiagvis, ddiagvis);
			ddiagvis.at(ddiag) = false;
			grid.at(x).at(y) = c;
		}

		++x, ++y;
	}
	// udiagvis.at(udiag) = false;
}

/*/

void extend_bishops(int udiag, int count, vector<vector<char>>& grid, vector<bool>& udiagvis, vector<bool>& ddiagvis) {
	int n = grid.size();

	for (int i=0; i<n; ++i) {
		grid.at(0).at(i) = '+';
	}

	for (int i=1; i<n-1; ++i) {
		grid.back().at(i) = '+';
	}

	maxboard = grid;
}

//*/


void extend_rooks(int row, int count, vector<vector<char>>& grid, const vector<bool>& rowskip, vector<bool>& colvis)
{
	int n = grid.size();

	if (count > maxscore) {
		maxscore = count;
		maxboard = grid;
	}

	if (row >= n) {
		return;
	}

	if (rowskip.at(row)) {
		extend_rooks(row+1, count, grid, rowskip, colvis);
		return;
	}

	for (int j=0; j<n; ++j) {
		if (colvis.at(j)) continue;

		char c = grid.at(row).at(j);
		grid.at(row).at(j) = 'x';
		colvis.at(j) = true;
		extend_rooks(row+1, count+1, grid, rowskip, colvis);
		colvis.at(j) = false;
		grid.at(row).at(j) = c;


		if (maxscore == n) {
			return;
		}
	}
}

int main() {
	int t; cin >> t;

	for (int i=1; i<=t; ++i) {
		int n,m; cin >> n >> m;

		vector<vector<char>> orig_grid(n, vector<char>(n, '.')), rook_grid(n, vector<char>(n, '.')), bishop_grid(n, vector<char>(n, '.'));

		vector<bool> rowvis(n, false);
		vector<bool> colvis(n, false);
		vector<bool> udiagvis(2*n-1, false);
		vector<bool> ddiagvis(2*n-1, false);
		
		int rcount = 0;
		int bcount = 0;

		for (int i=0; i<m; ++i) {
			char c;
			int x, y;

			cin >> c >> x >> y;
			--x, --y;

			if (c == 'x' || c == 'o') {
				orig_grid.at(x).at(y) = c;
				rook_grid.at(x).at(y) = 'x';
				rowvis.at(x) = true;
				colvis.at(y) = true;
				++rcount;
			}

			if (c == '+' || c == 'o') {
				orig_grid.at(x).at(y) = c;
				bishop_grid.at(x).at(y) = '+';
				udiagvis.at(x+y) = true;
				ddiagvis.at((n-1) + (x-y)) = true;
				++bcount;
			}
		}

		maxscore = 0;
		extend_bishops(0, bcount, bishop_grid, udiagvis, ddiagvis);
		bishop_grid = maxboard;

		maxscore = 0;
		extend_rooks(0, rcount, rook_grid, rowvis, colvis);
		rook_grid = maxboard;

		// debug(orig_grid);
		// debug(rook_grid);
		// debug(bishop_grid);

		int score = 0;
		int ucount = 0;
		stringstream ss;

		for (int i=0; i<n; ++i) {
			for (int j=0; j<n; ++j) {
				bool has_rook = rook_grid.at(i).at(j) == 'x';
				bool has_bishop = bishop_grid.at(i).at(j) == '+';
				bool has_queen = has_rook && has_bishop;

				char oc = orig_grid.at(i).at(j);
				char nc = '.';
				if (has_queen) nc = 'o';
				else if (has_bishop) nc = '+';
				else if (has_rook) nc = 'x';

				bool has_changed = (oc != nc);

				score += has_rook;
				score += has_bishop;
				ucount += has_changed;

				if (!has_changed) {
					continue;
				}

				if (has_queen) {
					ss << "o " << (i+1) << " " << (j+1) << "\n";
				} else if (has_rook) {
					ss << "x " << (i+1) << " " << (j+1) << "\n";
				} else if (has_bishop) {
					ss << "+ " << (i+1) << " " << (j+1) << "\n";
				}
			}
		}

		cout << "Case #" << i << ": " << score << " " << ucount << "\n" << ss.str();
	}

}