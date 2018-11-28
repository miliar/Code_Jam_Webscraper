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
	int cs = 0, t;
	cin >> t;
	string str;
	while (t-- && cin >> str) {
		int ans = 1, idx = -1;
		rep(j, siz(str) - 1) if (str[j] > str[j + 1]) {
			idx = j;
			break;
		}
		if (idx != -1) {
			while (idx >= 0) {
				--str[idx--];
				if (idx >= 0 && str[idx] <= str[idx + 1])
					break;
			}
			++idx;
			if (str[0] == '0') {
				rep(j, siz(str))
					str[j] = '9';
				str.pop_back();
			}
			else Rep(j, idx + 1, siz(str))
				str[j] = '9';
		}
		cout << "Case #" << ++cs << ": " << str << endl;
	}
	return 0;
}