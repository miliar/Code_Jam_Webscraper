//============================================================================
// Name        : C.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <string.h>
#include <memory.h>
#include <math.h>
using namespace std;
#define MAXN 1010
#define oo 1e9
#define MOD 1000000007
#define EPS 1e-8
typedef long long LL;
int k[MAXN], s[MAXN];
bool ok(char a, char b) {
	if (a == 'R') {
		return b == 'B' || b == 'G' || b == 'Y';
	}
	if (a == 'Y') {
		return b == 'R' || b == 'B' || b == 'V';
	}
	if (a == 'B') {
		return b == 'R' || b == 'Y' || b == 'O';
	}
	if (a == 'V') {
		return b == 'Y';
	}
	if (a == 'O') {
		return b == 'B';
	}
	if (a == 'G') {
		return b == 'R';
	}
	return false;
}
bool check(string str) {
	for (int i = 0; i < (int) str.length(); ++i) {
		if (!ok(str[i], str[(i + 1) % str.length()])) {
			return false;
		}
	}
	return true;
}
string ans;
void gao(char ch, int cnt) {
	bool flag = true;
	while (flag) {
		flag = false;
		for (int i = 0; i < (int) ans.length() && cnt > 0; ++i) {
			char a = ans[i];
			char b = ans[(i - 1 + ans.length()) % ans.length()];
			if (!ok(a, b) && ok(a, ch) && ok(b, ch)) {
				ans = ans.substr(0, i) + ch + ans.substr(i);
				flag = true;
				--cnt;
				break;
			}
		}
	}
	flag = true;
	while (flag) {
		flag = false;
		for (int i = 1; i < (int) ans.length() && cnt > 0; ++i) {
			char a = ans[i];
			char b = ans[(i - 1 + ans.length()) % ans.length()];
			if (ok(a, ch) && ok(b, ch)) {
				ans = ans.substr(0, i) + ch + ans.substr(i);
				flag = true;
				--cnt;
				break;
			}
		}
	}
	for (int i = 0; i < cnt; ++i) {
		ans += ch;
	}
}
void f(char a, int &x, char b, int &y) {
	for (int i = 0; i < x; ++i) {
		if (y > 0) {
			y--;
			ans += b;
		}
		ans += a;
	}
	if (x > 0 && y > 0) {
		y--;
		ans += b;
	}
}
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		ans = "";
		f('V', v, 'Y', y);
		f('O', o, 'B', b);
		f('G', g, 'R', r);
		gao('R', r);
		gao('Y', y);
		gao('B', b);
		if (!check(ans)) {
			ans = "IMPOSSIBLE";
		}
		printf("Case #%d: ", t);
		cout << ans << endl;
	}
	return 0;
}
