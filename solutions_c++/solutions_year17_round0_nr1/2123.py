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
	int k;
	string s;
	cin >> s >> k;
	int ans = 0;
	for (int i = 0; i + k - 1 < (int)s.length(); i++) {
		if (s[i] == '-') {
			ans++;
			for (int j = 0; j < k; j++) {
				if (s[i+j] == '+') {
					s[i+j] = '-';
				} else {
					s[i+j] = '+';
				}
			}
		}
	}
	bool fl = true;
	for (int i = 0; i < (int)s.length(); i++) {
		if (s[i] != '+') {
			fl = false;
		}
	}
	if (!fl) {
		cout << "IMPOSSIBLE\n";
	} else {
		cout << ans << "\n";
	}
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
		solve();
	}
	
	return 0;
}
