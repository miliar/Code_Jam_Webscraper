// hello!
#include <iostream>
#include <tuple>
#include <sstream>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <memory>
#include <array>

using namespace std;

typedef vector<vector<char> > mat;

void solve(int rows, int cols, mat &cake)
{
	vector<bool> empty(rows);

	for (int r = 0; r < rows; ++r) {
		char last = '?';
		for (int c = 0; c < cols; ++c) {
			char in = cake[r][c];
			if (in == '?' && last != '?') {
				cake[r][c] = last;
			} else if (in != '?' && last == '?') {
				for (int bakc = c - 1; bakc >= 0; --bakc) {
					cake[r][bakc] = in;
				}
			}
			if (in != '?')
				last = in;
		}
		if (last == '?')
			empty[r] = true;
	}

	for (int r = 0; r < rows; ++r) {
		if (empty[r]) {
			for (int c = 0; c < cols; ++c) {
				if (r == 0) {
					int ri = r + 1;
					while (empty[ri]) ++ri;
					cake[r][c] = cake[ri][c];
				} else {
					cake[r][c] = cake[r - 1][c];
				}
				
			}
		}
	}
}

//bool verify(mat &cake)
//{
//	set<c>
//}

int main(int argc, char *argv[])
{
    if (argc > 1) freopen(argv[1], "r", stdin);
    if (argc > 2) freopen(argv[2], "w", stdout);

    int numCases;
    cin >> numCases;

    int casei = 0;
	int rows, cols;
    while (++casei, cin >> rows >> cols) {


		
		mat cake(rows);
		for (auto &r : cake) {
			r.resize(cols);
		}
		for (int r = 0; r < rows; ++r) {
			for (int c = 0; c < cols; ++c) {
				char ch;
				cin >> ch;
				cake[r][c] = ch;
			}
		}

		solve(rows, cols, cake);

		cout << "Case #" << casei << ":" << endl;
		for (int r = 0; r < rows; ++r) {
			for (int c = 0; c < cols; ++c) {
				cout << cake[r][c];
			}
			cout << endl;
		}
    }

    return 0;
}