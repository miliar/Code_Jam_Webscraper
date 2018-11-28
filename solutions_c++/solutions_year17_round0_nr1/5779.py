//~In The Name Of Allah~//
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <math.h>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <string.h>
#include <cstdio>
#include <sstream>
#include <fstream>
#include <functional>
#include <stack>
#include <utility> 
#include <set>
#include <list>
#include <queue>
#include <bitset>
#include <time.h>
#include <complex>

using namespace std;

#define read freopen("in.txt", "r", stdin)
#define write freopen("out.txt", "w", stdout)
#define all(_) _.begin(), _.end()
#define rall(_) _.rbegin(), _.rend()
#define rep(i, j) for (int i = 0; i < j; i++)
#define Rep(i, j, k) for (int i = j; i < k; i++)
#define siz(_) (int)_.size()
#define ll long long
#define endl '\n'
#define ff fflush(stdout)

const double PI = 2.0 * acos(0.0);
const int MOD = 1e9 + 7;
const int oo = MOD;

typedef pair<int, int> pii;
typedef pair<string, string> pss;

ll gcd(ll x, ll y) { return !y ? x : gcd(y, x%y); }

int main() {
	read, write;
	int t, k, cs = 0;
	string str;
	cin >> t;
	while (t-- && cin >> str >> k) {
		int cnt = 0, ans = 0;
		rep(i, siz(str) - k + 1) if (str[i] == '-') {
			++ans;
			Rep(j, i, i + k) if (str[j] == '-')
				str[j] = '+';
			else
				str[j] = '-';
		}
		rep(i, siz(str)) if (str[i] == '+')
			++cnt;
		cout << "Case #" << ++cs << ": ";
		if (cnt == siz(str))
			cout << ans << endl;
		else
			puts("IMPOSSIBLE");
	}
	return 0;
}