#include <bits/stdc++.h>

using namespace std;

#define REP(i, N) for (int (i) = 0; (i) < (N); ++(i))
#define READALL(c) for (auto &e : c) { cin >> e; }
#define PRINTALL(c) for (const auto &e : c) { cout << e << "\t"; } cout << "\n";

template <typename T>
using V = vector<T>;

int N, R, Y, B, O, G, Vi;

unordered_map<int, bool> DPT[3][3][1001][1001];

bool f(int r, int y, int b, int cfirst, int clast) {
	if (r < 0 || y < 0 || b < 0)
		return 0;
	int cnt = r+y+b;
	if (cnt == 0) {
		return 1;
	}
	if (DPT[cfirst][clast][r][y].count(b))
		return DPT[cfirst][clast][r][y][b];
	bool ans = 0;
	unordered_set<int> opts = {0,1,2};
	if (cnt == 1)
		opts.erase(cfirst);
	opts.erase(clast);
	for (int o : opts) {
		switch (o) {
			case 0: ans = ans || f(r-1,y,b,cfirst,0); break;
			case 1: ans = ans || f(r,y-1,b,cfirst,1); break;
			case 2: ans = ans || f(r,y,b-1,cfirst,2); break;
		}
	}
	return DPT[cfirst][clast][r][y][b] = ans;
}

string cols;
void trace(int r, int y, int b, int cfirst, int clast) {
	if (r < 0 || y < 0 || b < 0)
		return;
	int cnt = r+y+b;
	if (cnt == 0) {
		return;
	}
	bool ans = 0;
	unordered_set<int> opts = {0,1,2};
	if (cnt == 1)
		opts.erase(cfirst);
	opts.erase(clast);
	for (int o : opts) {
		switch (o) {
			case 0: 
				if (f(r-1,y,b,cfirst,0)) {
					cols.push_back('R');
					trace(r-1,y,b,cfirst,0);
					return;
				}
				break;
			break;
			case 1: 
				if (f(r,y-1,b,cfirst,1)) {
					cols.push_back('Y');
					trace(r,y-1,b,cfirst,1);
					return;
				}
				break;
			case 2:
				if (f(r,y,b-1,cfirst,2)) {
					cols.push_back('B');
					trace(r,y,b-1,cfirst,2);
					return;
				}
				break;
		}
	}
}

bool check(string s) {
	int r = 0, b = 0, y = 0;
	for (char c : s) {
		if (c == 'R') {
			r++;
		} else if (c == 'B') {
			b++;
		} else {
			++y;
		}
	}
	assert(R == r && B == b && y == Y);

}

void solve() {
	cin >> N >> R >> O >> Y >> G >> B >> Vi;
	if (N == 1) {
		if (R) {
			cout << "R" << endl;
		} else if (Y) {
			cout << "Y" << endl;
		} else {
			cout << "B" << endl;
		}
		return;
	}
	// REP(a, 3) {
	// 	REP(b, 3) {
	// 		REP(r, R+1) {
	// 			REP(y, Y+1) {
	// 				DPT[a][b][r][y].clear();
	// 			}
	// 		}
	// 	}
	// }
	bool g = 0;
	for (int c = 0; c < 3; ++c) {
		switch (c) {
			case 0: g = g || f(R-1,Y,B,c,c); break;
			case 1: g = g || f(R,Y-1,B,c,c); break;
			case 2: g = g || f(R,Y,B-1,c,c); break;
		}
		// g = g || f(R,Y,B,c,c);
	}
	if (!g) {
		cout << "IMPOSSIBLE" << endl;
	} else {
		cols = "";
		bool d = 0;
		for (int c = 0; c < 3 && !d; ++c) {
			switch (c) {
				case 0: 
					if (f(R-1,Y,B,c,c)) {
						d = 1;
						cols.push_back('R');
						trace(R-1, Y, B, c, c);
					}
					break;
				case 1:
					if (f(R,Y-1,B,c,c)) {
						cols.push_back('Y');
						d = 1;
						trace(R, Y-1, B, c, c);
					}
					break;
				case 2:
					if (f(R,Y,B-1,c,c)) {
						d = 1;
						cols.push_back('B');
						trace(R, Y, B-1, c, c);
					}
					break;
			}
			// g = g || f(R,Y,B,c,c);
		}
		// check(cols);
		cout << cols << endl;
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T;
	cin >> T;

	REP(tc, T) {
		cout << "Case #" << (tc+1) << ": ";
		solve();
	}
}