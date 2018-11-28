#include <bits/stdc++.h>
#include <stdint.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

typedef uint8_t byte;
typedef int16_t i16;
typedef uint16_t ui16;
typedef int32_t i32;
typedef uint32_t ui32;
typedef int64_t i64;
typedef uint64_t ui64;
typedef long double ld;
typedef pair<int, int> Pii;

template <typename T>
using V = vector<T>;

typedef V<int> Vi;

template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

template <typename K, typename V>
using ordered_map = tree<K, V, less<K>, rb_tree_tag, tree_order_statistics_node_update>;

#ifndef M_PI
#	define M_PI 3.14159265358979323846
#endif

#define fi first
#define se second

int gcdex(int a, int b, int &x, int &y) {
	if (a == 0) {
		x = 0;
		y = 1;
		return b;		
	}

	int x1, y1;
	int g = gcdex(b % a, a, x1, y1);
	x = y1 - (b / a) * x1;
	y = x1;

	return g;
}

#define MOD 1000000007
inline int ADD_MOD(int a, int b) { return (a + b) % MOD; }
inline int MUL_MOD(int a, int b) { return (i64(a) * b) % MOD; }
inline int SUB_MOD(int a, int b) { return a >= b ? a - b : a + MOD - b; }
int DIV_MOD(int a, int b) {
	int x, y;
	gcdex(b, MOD, x, y);
	
	int b1 = (x % MOD + MOD) % MOD;
	return MUL_MOD(a, b1);
}

const ld EPS = 1. / 1e9;
inline bool EPS_EQUAL(ld a, ld b) { return abs(a - b) <= EPS; }
inline bool EPS_LESS(ld a, ld b) { return b - a > EPS; }
inline bool EPS_GREATER(ld a, ld b) { return a - b > EPS; }

const int INF = 1e9;
const i64 INF64 = 2e18;

char t[100][100];
set<Pii> added;

int calc_sum(int n) {
	int s = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (t[i][j]) {
				s += t[i][j] == 'o' ? 2 : 1;
			}
		}
	}
	return s;
}

void update(int r, int c, char ch) {
	t[r][c] = ch;
	added.insert({r, c});
}

void solve() {
	memset(t, 0, sizeof(t));
	added.clear();

	int n, m;
	cin >> n >> m;

	for (int i = 0; i < m; ++i) {
		char ch;
		int r, c;
		cin >> ch >> r >> c;
		--r, --c;

		t[r][c] = ch;
	}

	int xp, zp;
	xp = zp = -1;

	for (int i = 0; i < n; ++i) {
		if (!t[0][i]) {
			zp = i;
		} else if (t[0][i] != '+') {
			xp = i;
		}
	}

	if (xp < 0 && zp >= 0) {
		xp = zp;
		update(0, zp, 'x');
	}

	// fill diagonals
	if (xp >= 0) {
		for (int i = 0; i < n; ++i) {
			if (!t[0][i]) update(0, i, '+');
		}

		for (int i = 1; i < n; ++i) {
			if (xp + i < n) {
				update(i, xp + i, 'x');
			} else {
				update(i, n - i - 1, 'x');
			}
		}
	} else {
		for (int i = 1; i < n; ++i) {
			update(i, i, 'x');
		}
	}

	// fill last row
	for (int i = 1; i < n - 1; ++i) {
		update(n - 1, i, '+');
	}

	// add 'o'
	if (xp >= 0 && t[0][xp] != 'o') {
		update(0, xp, 'o');
	} else if (xp < 0) {
		update(0, 0, 'o');
	}

	cout << calc_sum(n) << " " << added.size() << endl;
	for (auto &i : added) {
		cout << t[i.fi][i.se] << " " << i.fi + 1 << " " << i.se + 1 << endl;
	}

	// for (int i = 0; i < n; ++i) {
	// 	for (int j = 0; j < n; ++j) {
	// 		cout << (t[i][j] ? t[i][j] : '.');
	// 	}
	// 	cout << endl;
	// }
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.precision(15);

	int tn;
	cin >> tn;

	for (int ti = 0; ti < tn; ++ti) {
		cout << "Case #" << (ti + 1) << ": ";
		solve();
	}

	return 0;
}
