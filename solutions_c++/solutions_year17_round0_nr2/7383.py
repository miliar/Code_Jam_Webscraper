#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <string>
#include <set>
#include <climits>
#include <cstdio>
#include <iomanip>
#include <iterator>
#include <deque>
#include <map>
#include <cassert>
#include <ctime>

// #include <bits/stdc++.h>
#include <iostream>

using namespace std;

#define pb push_back
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define size(a) (int)a.size()
typedef long long ll;
typedef long double ld;
const int inf = 2e9;
const long double eps = 0.000001;
const long long mod = 1e9 + 7;
const long double PI = 3.14159265359;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	#if _SLOVO
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#else
		//freopen(".in", "r", stdin);
		//freopen(".out", "w", stdout);
	#endif

	int t;
	cin >> t;
	int x = 1;
	while (t--) {
		cout << "Case #" << x << ": ";
		x++;
		string s;
		cin >> s;
		int g = 0;
		int n = size(s);
		vector < int > a(n);
		for (int i = 0; i < n; i++) {
			a[i] = s[i] - '0';
			g *= 10;
			g += a[i];
		}
		vector < int > r(n);
		bool less = false;
		for (int i = 0; i < n; i++) {
			if (less) {
				r[i] = 9;
				continue;
			}
			for (int c = 9; c >= 0; c--) {
				bool can = true;
				for (int j = i; j < n; j++) {
					if (c > a[j]) can = false;
					if (c < a[j]) break;
				}
				if (can) {
					if (c < a[i]) less = true;
					r[i] = c;
					break;
				}
			}
		}

		// ll ans = 0;

		bool nz = false;
		for (int i = 0; i < n; i++) {
			if (r[i] != 0) nz = true;
			if (!nz) continue;
			cout << r[i];
			// ans *= 10;
			// ans += r[i];
		}
		// cout << ans;


		// for (int i = ans + 1; i <= g; i++) {
		// 	int z = i;
		// 	int pz = inf;
		// 	bool good = true;
		// 	while (z > 0) {
		// 		if ((z % 10) > pz) good = false;
		// 		pz = (z % 10);
		// 		z /= 10;
		// 	}
		// 	if (good) {
		// 		cout << "\n\nWARNING!!!\n\n";
		// 		cout << s << " " << i << "\n";
		// 		break;
		// 	}
		// }

		cout << "\n";
	}

	return 0;
}
