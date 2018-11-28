// @betaveros v1.1 :: vim:set fdm=marker syntax=cppc:
// #define NDEBUG
// #includes, using namespace std {{{
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
// #include <cinttypes> // C++11?
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <functional>
#include <new>
#include <algorithm>
#include <iostream>
using namespace std;
// }}}
// #defines, typedefs, constants {{{
#define fori(i,s,e) for(int i = s; i < ((int)e); i++)
#define fori0(i,e) for(int i = 0; i < ((int)e); i++)
#define fori1(i,e) for(int i = 1; i <= ((int)e); i++)
#define forui(i,s,e) for(unsigned int i = s; i < ((unsigned int)e); i++)
#define foruin(i,c) for(unsigned int i = 0; i < ((unsigned int)(c).size()); i++)
#define _conc(x,y) x ## y
#define _conc2(x,y) _conc(x,y)
#define repeat(n) fori(_conc2(_,__LINE__),0,n)
#define allof(s) (s).begin(), (s).end()
#define scan_d(x) scanf("%d",&(x))
#define scan_dd(x,y) scanf("%d%d",&(x),&(y))
#define scan_ddd(x,y,z) scanf("%d%d%d",&(x),&(y),&(z))
#define scan_dddd(x,y,z,w) scanf("%d%d%d%d",&(x),&(y),&(z),&(w))
#define pushb push_back
#define popb push_back

#ifdef NDEBUG
#define debug(code)
#define debugf(...) ((void)0)
#else
#define debug(code) code
#ifdef CDEBUG
#define debugf(...) fputs("\033[35m", stderr);fprintf(stderr, __VA_ARGS__);fputs("\033[0m", stderr)
#else
#define debugf(...) fprintf(stderr, __VA_ARGS__)
#endif
#endif
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector<int> Vint;
typedef vector<int>::iterator Vit;

// const int OO  = 1000 << 20;
// const int OO2 = 2000 << 20;
// const int       M7  = 1000000007;
// const int       M9  = 1000000009;
// const long long M7L = 1000000007L;
// }}}
// dump, min/maxify {{{
template <class T> void dumpBetween(const T & a, const T & b) {
	for (T it = a; it != b; it++) cout << *it << " ";
	cout << endl;
}
template <class T> void dumpAll(const T & a) { dumpBetween(allof(a)); }
template <class T> void minify(T & a, const T & b) { if (a > b) a = b; }
template <class T> void maxify(T & a, const T & b) { if (a < b) a = b; }
// }}}

int nRows, nCols;
char grid[88][88];
char forcedGrid[88][88];

void readInput() {
	scan_dd(nRows, nCols);
	fori (i, 0, nRows) {
		scanf("%s", grid[i]);
		grid[i][nCols] = '\0';
		forcedGrid[i][nCols] = '\0';
	}
}

bool force(int i, int j, char beam) {
	if (forcedGrid[i][j] == '?' || forcedGrid[i][j] == beam) {
		forcedGrid[i][j] = beam;
		return true;
	}
	return false;
}

bool isBeam(char c) { return c == '|' || c == '-'; }

typedef struct Vision {
	int row, col; char content;
	bool beam() { return isBeam(content); }
} Vision;

Vision see(int r, int c, int rd, int cd) {
	while (true) {
		r += rd;
		c += cd;
		if (0 <= r && r < nRows && 0 <= c && c < nCols) {
			if (grid[r][c] != '.') {
				return (Vision) { .row = r, .col = c, .content = grid[r][c] };
			}
		} else {
			return (Vision) { .row = r, .col = c, .content = '#' };
		}
	}
}

#define solveForce(i, j, c) if (!force(i, j, c)) return false

typedef pair<Vision, char> Literal;
typedef pair<Literal, Literal> Constraint;

char rotate(char c) {
	switch (c) {
		case '|': return '-';
		case '-': return '|';
	}
	throw "gg rotate";
}

int check(const Literal & lit) {
	// 1 if known true, 0 if unknown, -1 if known false
	if (forcedGrid[lit.first.row][lit.first.col] == lit.second) {
		return 1;
	} else if (forcedGrid[lit.first.row][lit.first.col] == '?') {
		return 0;
	} else {
		assert(forcedGrid[lit.first.row][lit.first.col] == rotate(lit.second));
		return -1;
	}
}

bool solve() {
	fori (i, 0, nRows) {
		fori (j, 0, nCols) {
			forcedGrid[i][j] = isBeam(grid[i][j]) ? '?' : grid[i][j];
		}
	}
	vector<Constraint> constraints;
	fori (i, 0, nRows) {
		fori (j, 0, nCols) {
			char cur = grid[i][j];
			if (isBeam(cur)) {
				// Check for forcedness.
				for (int rd = -1; rd <= 1; rd += 2) {
					Vision v = see(i, j, rd, 0);
					if (v.beam()) {
						solveForce(i, j, '-');
						solveForce(v.row, v.col, '-');
					}
				}
				for (int cd = -1; cd <= 1; cd += 2) {
					Vision v = see(i, j, 0, cd);
					if (v.beam()) {
						solveForce(i, j, '|');
						solveForce(v.row, v.col, '|');
					}
				}
			} else if (cur == '.') {
				// Check for necessity of coverage.
				vector<Literal> possibleCovers;
				for (int rd = -1; rd <= 1; rd += 2) {
					Vision v = see(i, j, rd, 0);
					if (v.beam()) {
						possibleCovers.push_back(make_pair(v, '|'));
					}
				}
				for (int cd = -1; cd <= 1; cd += 2) {
					Vision v = see(i, j, 0, cd);
					if (v.beam()) {
						possibleCovers.push_back(make_pair(v, '-'));
					}
				}
				switch (possibleCovers.size()) {
					case 0: return false;
					case 1:
							do {
								auto p = possibleCovers[0];
								solveForce(p.first.row, p.first.col, p.second);
							} while (0);
							break;
					case 2:
							if (possibleCovers[0].second == possibleCovers[1].second) return false;
							constraints.push_back(make_pair(
										possibleCovers[0],
										possibleCovers[1]));
							break;
					default:
							return false;
				}
			}
		}
	}
	// for the hardcore version we need to solve a 2-SAT
	// but for the easy version, if no conflicts yet,
	// every still non-certain space is coverable by two lasers
	for (Constraint & con : constraints) {
		int c1 = check(con.first);
		int c2 = check(con.second);
		if (c1 == 1 || c2 == 1) {
			// no prob
			continue;
		} else if (c1 == -1 && c2 == -1) {
			// gg failed
			return false;
		} else if (c1 == -1 && c2 == 0) {
			solveForce(con.second.first.row, con.second.first.col, con.second.second);
		} else if (c1 == 0 && c2 == -1) {
			solveForce(con.first.first.row, con.first.first.col, con.first.second);
		} else {
			assert(c1 == 0 && c2 == 0);
		}
	}

	fori (i, 0, nRows) {
		fori (j, 0, nCols) {
			if (forcedGrid[i][j] == '?') {
				forcedGrid[i][j] = '-';
			}
		}
	}
	return true;
}


void tc(int tci) {
	readInput();
	printf("Case #%d: ", tci);
	if (solve()) {
		printf("POSSIBLE\n");
		fori (i, 0, nRows) {
			puts(forcedGrid[i]);
		}
	} else {
		printf("IMPOSSIBLE\n");
	}
}

int main() {
	int tcn;
	scanf("%d", &tcn);
	fori (i, 0, tcn) tc(i+1);
}
