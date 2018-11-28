#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <cstdlib>
#include <memory>
#include <queue>
#include <cassert>
#include <cmath>
#include <ctime>
#include <complex>
#include <bitset>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <numeric>

using namespace std;

#define ws ws_____________________
#define y1 y1_____________________
#define y0 y0_____________________
#define left left_________________
#define right right_______________
#define next next_________________
#define prev prev_________________
#define hash hash_________________

#define pb push_back
#define fst first
#define snd second
#define mp make_pair 
#define sz(C) ((int) (C).size())
#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; --i)
#define all(C) begin(C), end(C)

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int,int> pii;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vii;
typedef long double ld;
typedef complex<double> cd;

#define FILE_NAME "a"

const string FAIL = "IMPOSSIBLE";

int N, R, O, Y, G, B, V;

bool read() {
	if  (scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V) < 7) {
		return 0;
	}
	return 1;
}


string small_solve() {
	vector<pair<int, char>> cs;
	cs.pb(mp(R, 'R'));
	cs.pb(mp(Y, 'Y'));
	cs.pb(mp(B, 'B'));
	sort(all(cs));
	reverse(all(cs));

	string res = string(cs[0].fst, cs[0].snd);
	for (int i = 1; i < sz(cs); ++i) {
		string nres;
		int have = cs[i].fst;
		char ch = cs[i].snd;
		forn(i, sz(res)) {
			if  (have > 0) {
				nres += ch;
				--have;
			}
			nres += res[i];
		}
		res.swap(nres);
	}

	forn(i, sz(res)) {
		if  (res[i] == res[(i + 1) % sz(res)]) {
			return FAIL;
		}
	}
	return res;
}

string new_small_solve() {
	vector<pair<int, char>> cs;
	cs.pb(mp(R, 'R'));
	cs.pb(mp(Y, 'Y'));
	cs.pb(mp(B, 'B'));
	sort(all(cs));
	reverse(all(cs));

	string res = string(cs[0].fst, cs[0].snd);
	for (int i = 1; i < sz(cs); ++i) {
		string nres;
		int have = cs[i].fst;
		char ch = cs[i].snd;
		forn(i, sz(res)) {
			if  (have > 0) {
				nres += ch;
				--have;
			}
			nres += res[i];
		}

		res.swap(nres);

		if  (i == 1) {
			auto last = res.back();
			res.pop_back();
			reverse(all(res));
			res.pb(last);
		}
	}

	assert(sz(res) == N);

	forn(i, sz(res)) {
		if  (res[i] == res[(i + 1) % sz(res)]) {
			return FAIL;
		}
	}
	return res;
}

string solve() {
	auto old = small_solve();
	auto nw = new_small_solve();
	if  (old != nw) {
		cerr << "FOUND" << endl;
	}
	return nw;
}

int main() {
#ifdef LOCAL
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
#endif

	int T;
	scanf("%d", &T);
	forn(t, T) {
		assert(read());
		printf("Case #%d: %s\n", t + 1, solve().data());
	}

#ifdef LOCAL
	cerr.precision(5);
	cerr << "Time: " << fixed << (double) clock() / CLOCKS_PER_SEC << endl;
#endif
	return 0;
}

