#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define debug(a) cerr<< #a << " = " << (a) << endl;
typedef long long ll;
typedef pair<int , int > pii;
typedef vector<int > vi;
typedef vector<vi > vvi;
template <typename T> ostream& operator <<( ostream& o, vector <T>& v) {
for (auto& a: v) o << a << ' ';
	return o;
}

char z[250][250];

void do_case() {
	int r,c;
	cin >> r >> c;
	
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cin >> z[i][j];
		}
	}
	bool seen[256];
	fill(seen, seen+256, false);

	/*
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (z[i][j] != '?' && !seen[z[i][j]]) {
				seen[z[i][j]] = true;
				char cur = z[i][j];
				// extend down
				int top = i;
				int bot = i;
				int left = j;
				int right = j;
				while (z[bot][j] == cur || z[bot][j] == '?') {
					z[bot][j] = cur;
					bot++;
				}
				// extend right
				while (true) {
					bool bad = false;
					// check whether right works
					for (int y = top; y <= bot; y++) {
						if (z[y][right+1] == cur || z[y][right+1] == '?') {
							continue;
						} else {
							bad = true;
							break;
						}
					}
					if (bad) {
						break;
					}
					// set
					for (int y = top; y <= bot; y++) {
						z[y][right+1] = cur;
					}
					// inc
					right++;
				}
				// extend up
				while (top > 0) {
					bool bad = false;
					// check whether right works
					for (int x = left; x <= right; x++) {
						if (z[top-1][x] == cur || z[top-1][x] == '?') {
							continue;
						} else {
							bad = true;
							break;
						}
					}
					if (bad) {
						break;
					}
					// set
					for (int x = left; x <= right; x++) {
						z[top-1][x] = cur;
					}
					// inc
					top--;;
				}

				// extend left
				while (left > 0) {
					bool bad = false;
					for (int y = top; y <= bot; y++) {
						if (z[y][left-1] == cur || z[y][left-1] == '?') {
							continue;
						} else {
							bad = true;
							break;
						}
					}
					if (bad) {
						break;
					}
					// set
					for (int y = top; y <= bot; y++) {
						z[y][left-1] = cur;
					}
					// inc
					right++;
				}
			}
		}
	}
	*/
	while (true) {
		int best = 0;
		char bestc = '?';
		int btop = 0, bleft = 0, bbot = 0, bright = 0;

		for (int top = 0; top < r; top++) {
			for (int left = 0; left < c; left++) {
				for (int bot = top; bot < r; bot++) {
					for (int right = left; right < c; right++) {
						// do a check
						int area = (right - left + 1) * (bot - top + 1);
						if (area < best) {
							continue;
						}

						char cc = '?';
						bool bad = false;

						for (int y = top; y <= bot; y++) {
							if (bad) break;
							for (int x = left; x <= right; x++) {
								if (z[y][x] != '?') {
									if (cc != '?') {
										bad = true;
										break;
									} else {
										cc = z[y][x];
									}
								}
							}
						}
						if (bad) continue;
						if (cc == '?') continue;
						if (seen[cc]) continue;
						btop = top;
						bbot = bot;
						bleft = left;
						bright = right;
						best = area;
						bestc = cc;
					}
				}
			}
		}

		// debug(best);

		
		if (best == 1 || best == 0) {
			for (int i = 0; i < r; i++) {
				for (int j = 0; j < c; j++) {
					cout << z[i][j];
				}
				cout << endl;
			}
			return;
		}
		assert(bestc != '?');

		for (int y = btop; y <= bbot; y++) {
			for (int x = bleft; x <= bright; x++) {
				z[y][x] = bestc;
			}
		}
		seen[bestc] = true;
		
	}
}

int main () {
	ios::sync_with_stdio (0);cin.tie (0);
	int cases;
	cin >> cases;
	for (int c = 0; c < cases; c++) {
		cout << "Case #" << (c+1) << ":";
		cout << endl;
		do_case();
	}
}
