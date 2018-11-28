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
	ll n, k;
	cin >> n >> k;
	queue < pair < ll, ll > > q;
	q.push(mp(n, 1));
	ll ans = 0;
	while (k > 0) {
		auto f = q.front(); q.pop();
		k -= f.snd;
		ans = f.fst;
		ll x = f.fst - 1;
		if (x & 1) {
			q.push(mp(x/2+1, f.snd));
			q.push(mp(x/2, f.snd));
		} else {
			q.push(mp(x/2, 2*f.snd));
		}
	}
	cout << ans / 2 << " " << (ans-1) / 2 << "\n";
}

void solve2() {
	ll n, k;
	cin >> n >> k;
	queue < ll > q;
	q.push(n);
	map < ll, ll > m;
	m[n] = 1;
	ll ans = 0;
	while (k > 0) {
		ll x = q.front(); q.pop();
		k -= m[x];
		x--;
		ans = x;
		if (m[x-x/2] == 0) {
			q.push(x-x/2);
		}
		m[x-x/2] += m[x+1];
		if (m[x/2] == 0) {
			q.push(x/2);
		}
		m[x/2] += m[x+1];
	}
	cout << (ans + 1) / 2 << " " << ans / 2 << "\n";
}

int main() {
	//srand(time(NULL));
	#ifdef LOCAL	
		//gen();
		freopen("b.in", "r", stdin);
		freopen("b.out", "w", stdout);
		cout << endl << endl;
	#else
		//freopen("whats.in", "r", stdin);
		//freopen("whats.out", "w", stdout);
	#endif
	//check();
	
	ios_base::sync_with_stdio(false);
	
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		cout << "Case #" << test << ": ";
		solve2();
	}
	
	return 0;
}
