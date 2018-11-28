// @betaveros :: vim:set fdm=marker syntax=cppc:
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
#define debugf(...) fprintf(stderr, __VA_ARGS__)
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

const int N = 108;
bool rooks[N][N];
bool bishops[N][N];
bool differences[N][N];
bool rookRows[2*N];
bool rookCols[2*N];
bool bishopSums[2*N];
bool _bishopDiffs[2*N], *bishopDiffs = _bishopDiffs + N;

int n, k;

void falseToTrue(bool & b) {
	assert(!b);
	b = true;
}

void readInput() {
	scan_dd(n, k);
	fori (i, 0, n) {
		fori (j, 0, n) {
			rooks[i][j] = bishops[i][j] = differences[i][j] = false;
		}
	}
	fori (i, 0, 2*N) {
		rookRows[i] = rookCols[i] = bishopSums[i] = _bishopDiffs[i] = false;
	}
	repeat (k) {
		char c;
		scanf(" %c", &c);
		int i, j;
		scan_dd(i, j);
		i--; j--;
		if (c == 'o' || c == '+') {
			falseToTrue(bishops[i][j]);
			falseToTrue(bishopSums[i + j]);
			falseToTrue(bishopDiffs[i - j]);
		}
		if (c == 'o' || c == 'x') {
			falseToTrue(rooks[i][j]);
			falseToTrue(rookRows[i]);
			falseToTrue(rookCols[j]);
		}
	}
}

void placeRooks() {
	int ri = 0, ci = 0;
	while (true) {
		while (ri < n && rookRows[ri]) { ri++; }
		while (ci < n && rookCols[ci]) { ci++; }
		if (ri == n || ci == n) {
			assert(ri == n && ci == n);
			return;
		}
		falseToTrue(rookRows[ri]);
		falseToTrue(rookCols[ci]);
		falseToTrue(rooks[ri][ci]);
		differences[ri][ci] = true;
	}
}

void placeBishop(int r, int c) {
	if (!bishopSums[r + c] && !bishopDiffs[r - c]) {
		falseToTrue(bishops[r][c]);
		falseToTrue(bishopSums[r + c]);
		falseToTrue(bishopDiffs[r - c]);
		differences[r][c] = true;
	}
}

void placeBishops() {
	fori (i, 0, n) {
		placeBishop(i, 0);
		placeBishop(0, i);
		placeBishop(i, n - 1);
		placeBishop(n - 1, i);
	}
}

vector<pair<int, int> > diffVector;

int score = 0;

void collectScoreAndDifferences() {
	score = 0;
	diffVector.clear();
	fori (i, 0, n) fori (j, 0, n) {
		if (rooks[i][j]) { score++; }
		if (bishops[i][j]) { score++; }
		if (differences[i][j]) {
			diffVector.push_back(make_pair(i, j));
		}
	}
}

char rookBishopChar(bool rk, bool bs) {
	return rk ? (bs ? 'o' : 'x') : (bs ? '+' : '.');
}

void tc(int tci) {
	readInput();
	
	placeRooks();
	placeBishops();
	collectScoreAndDifferences();

	printf("Case #%d: %d %lu\n", tci, score, diffVector.size());
	for (const pair<int, int> & p : diffVector) {
		printf("%c %d %d\n", rookBishopChar(rooks[p.first][p.second], bishops[p.first][p.second]), p.first + 1, p.second + 1);
	}
}

int main() {
	int tcn;
	scanf("%d", &tcn);
	fori (i, 0, tcn) tc(i+1);
}
