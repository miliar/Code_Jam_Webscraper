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
		int k;
		cin >> k;
		vector < int > a(size(s));
		for (int i = 0; i < size(s); i++) {
			if (s[i] == '-') a[i] = 1;
			else a[i] = 0;
		}

		int n = size(s);
		int q = 0;
		vector < int > d(n, 0);
		int cnt = 0;
		for (int i = n - 1; i >= 0; i--) {
			if (i - k + 1 < 0) break;
			if (q % 2 != a[i]) {
				cnt++;
				q++;
				d[i - k + 1]--;
			}
			q += d[i];
		}

		bool fl = false;
		for (int i = k - 2; i >= 0; i--) {
			if (q % 2 != a[i]) {
				cout << "IMPOSSIBLE\n";
				fl = true;
				break;
			}
			q += d[i];
		}
		if (fl) continue;
		cout << cnt << "\n";
	}

	return 0;
}
