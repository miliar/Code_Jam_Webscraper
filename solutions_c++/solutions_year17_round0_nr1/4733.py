#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <unordered_map>
#include <string.h>
#include <bitset>

#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define ll long long
#define forn(i, n) for (int i = 0; i < (int) (n); i++)
#define forlr(i, l, r) for (int i = (int) l; i <= (int) (r); i++)
#define forrl(i, r, l) for (int i = (int) r; i >= (int) (l); i--)

using namespace std;

ll const MOD = 1000000007;
ll const LLINF = 1000000000000000000;
int const INF = 1000000000;

int const MAXN = 200000;


bool good(string s) {
	forn(i, s.length()) {
		if (s[i] != '+') {
			return false;
		}
	}
	return true;
}


int main() {
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

	int t;
	cin >> t;

	forn(cur_t, t) {
		string s;
		int k;
		int res = 0;
		cin >> s >> k;
		forn(i, s.length() - k + 1) {
			if (s[i] == '-') {
				res++;
				forlr(j, i, i + k - 1) {
					if (s[j] == '-') {
						s[j] = '+';
					} else {
						s[j] = '-';
					}
				}
			}
		}
		if (good(s)) {
			cout << "Case #" << cur_t + 1 << ": " << res << "\n";
		} else {
			cout << "Case #" << cur_t + 1 << ": " << "IMPOSSIBLE\n";
		}
	}
	
	

	return 0;
}









