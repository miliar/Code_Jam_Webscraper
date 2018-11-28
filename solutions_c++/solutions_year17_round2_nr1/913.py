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

const ld INF = 1e18;

void solve() {
	int n, D;
	cin >> D >> n;
	ld ans = INF;
	for (int i = 0; i < n; i++) {
		int x, y;
		cin >> x >> y;
		ans = min(ans, (ld)D / ((D-x)*1./y));
	}
	cout.precision(10);
	cout << fixed << ans << "\n";
}


int main() {
	//srand(time(NULL));
	#ifdef LOCAL	
		//gen();
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
		//cout << endl << endl;
	#else
		//freopen("paratroopers.in", "r", stdin);
		//freopen("paratroopers.out", "w", stdout);
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
