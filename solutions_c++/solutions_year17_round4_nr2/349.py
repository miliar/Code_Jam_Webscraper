#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cassert>
#include <bitset>
#include <fstream>
#include <stack>
#include <cstdlib>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define fst first
#define snd second
#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double

template < typename T>
T sqr(T x) {
	return x * x;
}

template < typename T>
T abs(T x) {
	return x > 0 ? x : -x;
}

//////////////////////////////////////////////////

void solve() {
	int n, m, q;
	cin >> n >> m >> q;
	vector < vector < int > > pos(n + 1), players(m + 1);
	for (int i = 0; i < q; i++) {
		int x, y;
		cin >> x >> y;
		pos[x].pb(y);
		players[y].pb(x);
	}
	int maxi = 0;
	for (int i = 1; i <= m; i++) {
		maxi = max(maxi, (int)players[i].size());
	}
	int le = maxi, ri = q;
	while (le < ri) {
		int mi = (le + ri) / 2;
		int prv = 0;
		int ans = 0;
		for (int p = n; p >= 1; p--) {
			int nxt = prv + pos[p].size();
			if (nxt > mi) {
				nxt -= mi;
				if (nxt > prv) {
					ans += nxt - prv;
				}
				prv = nxt;
			} else {
				prv = 0;
			}
		}
		//cout << mi << " " << prv << "\n";
		if (prv == 0) {
			ri = mi;
		} else {
			le = mi + 1;
		}
	}
	int mi = le;
	int ans = 0, prv = 0;
	for (int p = n; p >= 1; p--) {
		int nxt = prv + pos[p].size();
		if (nxt > mi) {
			nxt -= mi;
			if (nxt > prv) {
				ans += nxt - prv;
			}
			prv = nxt;
		} else {
			prv = 0;
		}
	}
	cout << mi << " " << ans << "\n";
}

int main() {
	//srand(time(NULL));
	#ifdef LOCAL	
		//gen();
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
		//cout << endl << endl;
	#else
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
	#endif
	//check();
	
	//ios_base::sync_with_stdio(false);
	
	
	
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		cout << "Case #" << test << ": ";
		solve();
	}
	
	return 0;
}
