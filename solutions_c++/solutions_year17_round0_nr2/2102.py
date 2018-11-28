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
	string s;
	cin >> s;
	for (int i = 0; i < (int)s.length() - 1; i++) {
		if (s[i] > s[i+1]) {
			int j = i;
			while (j >= 0 && s[j] == s[i]) {
				j--;
			}
			j++;
			s[j]--;
			for (int k = j + 1; k < (int)s.length(); k++) {
				s[k] = '9';
			}
			for (int i = (s[0] == '0' ? 1: 0); i < (int)s.length(); i++) {
				cout << s[i];
			}
			cout << "\n";
			return;
		}
	}
	cout << s << "\n";
	return;
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
