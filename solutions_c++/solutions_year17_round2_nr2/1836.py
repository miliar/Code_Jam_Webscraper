#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <algorithm>
#include <iomanip>
#include <cstdio>

using namespace std;

struct inp_t {
	int n;
	int r,y,b,v,o,g;

	void state() {
		cout << n << " " << r << " " << o << " " << y << " " << g << " " << b << " " << v << endl;
	}
};

string solve(inp_t & inp) {

	std::stringstream sr;

	// RYB greed
	string result = "";
	string pos = "";
	if ((inp.y >= inp.r) && (inp.y >= inp.b)) {
		pos = "Y";
		inp.y -= 1;
	}
	else
	if ((inp.r >= inp.y) && (inp.r >= inp.b)) {
		pos = "R";
		inp.r -= 1;
	}
	else {
		pos = "B";
		inp.b -= 1;
	}

	while(true) {
		result += pos;
//		cout << "r:" << result << endl;
		if (pos == "R") {

			if (inp.g > 0) {
				// R-G.
				inp.g -= 1;
				pos = "G";
				continue;
			}

			if (inp.y + inp.b == 0) {
				// stop and check.
				if ((inp.v > 0) || (inp.o > 0))
					return "IMPOSSIBLE";

				if ((result[0] == 'O') ||
					(result[0] == 'V') ||
					(result[0] == 'R'))
				{
					return "IMPOSSIBLE";
				}

				return result;
			}

			if (inp.y == inp.b) {
				if (result[0] == 'B') {
					inp.b -= 1;
					pos = "B";
					continue;
				}
			}

			if (inp.y >= inp.b) {
				// R-Y.
				inp.y -= 1;
				pos = "Y";
				continue;
			}

			// R-B.
			inp.b -= 1;
			pos = "B";
			continue;
		}

		if (pos == "Y") {

			if (inp.v > 0) {
				// Y-V.
				inp.v -= 1;
				pos = "V";
				continue;
			}

			if (inp.r + inp.b == 0) {
				// stop and check.
				if ((inp.g > 0) || (inp.o > 0))
					return "IMPOSSIBLE";

				if ((result[0] == 'Y') ||
					(result[0] == 'G') ||
					(result[0] == 'O'))
				{
					return "IMPOSSIBLE";
				}

				return result;
			}

			if (inp.r == inp.b) {
				if (result[0] == 'B') {
					inp.b -= 1;
					pos = "B";
					continue;
				}
			}

			if (inp.r >= inp.b) {
				// Y-R.
				inp.r -= 1;
				pos = "R";
				continue;
			}

			// Y-B.
			inp.b -= 1;
			pos = "B";
			continue;
		}

		if (pos == "B") {

			if (inp.o > 0) {
				// B-O.
				inp.o -= 1;
				pos = "O";
				continue;
			}

			if (inp.y + inp.r == 0) {
				// stop and check.
				if ((inp.v > 0) || (inp.g > 0))
					return "IMPOSSIBLE";

				if ((result[0] == 'V') ||
					(result[0] == 'G') ||
					(result[0] == 'B'))
				{
					return "IMPOSSIBLE";
				}

				return result;
			}

			if (inp.y == inp.r) {
				if (result[0] == 'R') {
					inp.r -= 1;
					pos = "R";
					continue;
				}
			}

			if (inp.y >= inp.r) {
				// B-Y.
				inp.y -= 1;
				pos = "Y";
				continue;
			}

			// B-R.
			inp.r -= 1;
			pos = "R";
			continue;
		}

		if (pos == "G") {
			if (inp.r > 0) {
				// G-R.
				inp.r -= 1;
				pos = "R";
				continue;
			}

			if ((inp.v > 0) || (inp.y > 0) || (inp.b > 0) || (inp.o > 0))
				return "IMPOSSIBLE";

			if (result[0] == 'R') return result;
			else return "IMPOSSIBLE";
		}

		if (pos == "V") {
			if (inp.y > 0) {
				// V-Y.
				inp.y -= 1;
				pos = "Y";
				continue;
			}

			if ((inp.g > 0) || (inp.r > 0) || (inp.b > 0) || (inp.o > 0))
				return "IMPOSSIBLE";

			if (result[0] == 'Y') return result;
			else return "IMPOSSIBLE";
		}

		if (pos == "O") {
			if (inp.b > 0) {
				// O-B.
				inp.b -= 1;
				pos = "B";
				continue;
			}

			if ((inp.g > 0) || (inp.r > 0) || (inp.v > 0) || (inp.y > 0))
				return "IMPOSSIBLE";

			if (result[0] == 'B') return result;
			else return "IMPOSSIBLE";
		}
	}
}

int main() {
	int n;
	cin >> n;
	string x;
	getline(cin, x);
	for (int l = 1; l <= n; ++l) {
		inp_t inp;
		getline(cin, x);
		stringstream ss(x);
		ss >> inp.n >> inp.r >> inp.o >> inp.y >> inp.g >> inp.b >> inp.v;
		cout << "Case #" << l << ": " << solve(inp) << endl;
	}
	return 0;
}