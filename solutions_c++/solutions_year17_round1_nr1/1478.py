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
	int t, n, m, cs = 0;
	cin >> t;
	while (t-- && cin >> n >> m) {
		vector<string> in(n);
		rep(i, n)
			cin >> in[i];
		rep(i, m) rep(j, n) {
			if (in[j][i] != '?') {
				int idx = j - 1;
				while (idx > -1 && in[idx][i] == '?')
					in[idx--][i] = in[j][i];
				idx = j + 1;
				while (idx < n && in[idx][i] == '?')
					in[idx++][i] = in[j][i];
			}
		}
		rep(i, m) if (in[0][i] == '?') {
			int idx = i;
			while (idx >= 0 && in[0][idx] == '?')
				--idx;
			if (idx >= 0) {
				rep(j, n) Rep(k, idx + 1, i + 1)
					in[j][k] = in[j][k - 1];
			}
			else {
				int idx = i;
				while (idx < m && in[0][idx] == '?')
					++idx;
				rep(j, n) for (int k = idx - 1; k >= i; k--)
					in[j][k] = in[j][k + 1];
			}
		}
		cout << "Case #" << ++cs << ":\n";
		rep(i, n)
			cout << in[i] << endl;
	}
	return 0;
}