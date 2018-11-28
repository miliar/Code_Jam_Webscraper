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


ll n, k;

bool read() {
	if  (scanf("%lld%lld", &n, &k) < 2) {
		return 0;
	}
	return 1;
}

pll brut() {
	multiset<ll> lens;
	lens.insert(n);
	pll last;
	for (ll it = 0; it < k; ++it) {
		assert(!lens.empty());

		ll len = *lens.rbegin();
		lens.erase(lens.find(len));

		ll left = (len - 1) / 2;
		ll right = len - 1 - left;
		last = mp(max(left, right), min(left, right));

		if  (left > 0) {
			lens.insert(left);
		}
		if  (right > 0) {
			lens.insert(right);
		}
	} 

	return last;
}

pll smart() {
	map<ll, ll> M;
	M[n] = 1;
	pll last;
	ll old_k = k;
	while (k > 0) {
		assert(!M.empty());
		ll len = M.rbegin()->fst;
		ll cnt = M.rbegin()->snd;
		M.erase(len);

		ll times = min(k, cnt);
		k -= times;

		ll left = (len - 1) / 2;
		ll right = len - 1 - left;
		last = mp(max(left, right), min(left, right));

		if  (left > 0) {
			M[left] += times;
		}		
		if  (right > 0) {
			M[right] += times;
		}

		cnt -= times;
		if  (cnt > 0) {
			M[len] = cnt;
		}
	}

	k = old_k;
	return last;
}

pll solve() {
	auto sm = smart();
	// auto br = brut();
	// cerr << "sm = " << sm.fst << " " << sm.snd << ", br = " << br.fst << " " << br.snd << endl;
	// assert(sm == br);
	return sm;
}

int main() {
#ifdef LOCAL
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
#endif

	int T;
	scanf("%d\n", &T);
	forn(t, T) {
		assert(read());
		auto res = solve();
		printf("Case #%d: %lld %lld\n", t + 1, res.fst, res.snd);

		cerr << t << " " << T << endl;
	}

#ifdef LOCAL
	cerr.precision(5);
	cerr << "Time: " << fixed << (double) clock() / CLOCKS_PER_SEC << endl;
#endif
	return 0;
}

