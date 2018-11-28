#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

#define uchar unsigned char
#define ushort unsigned short
#define uint unsigned int
#define ull unsigned ll
#define ll long long
#define ull unsigned ll

#define E 2.718281828
#define PI 3.14159265358979323846264338328

using namespace std;

const int MAXN = 24 * 60;

int a1, a2;
bool flag1[MAXN], flag2[MAXN];

int dp1[MAXN][2 * MAXN + 1];
int dp2[MAXN][2 * MAXN + 1];

int get1(int m, int offset) {
	return dp1[m][offset + MAXN];
}

void set1(int m, int offset, int val) {
	dp1[m][offset + MAXN] = val;
}

int get2(int m, int offset) {
	return dp2[m][offset + MAXN];
}

void set2(int m, int offset, int val) {
	dp2[m][offset + MAXN] = val;
}

void solve() {
	cin >> a1 >> a2;
	for (int i = 0; i < MAXN; i++)
		flag1[i] = flag2[i] = false;
	for (int i = 0; i < a1; i++) {
		int from, to;
		cin >> from >> to;
		for (int j = from; j < to; j++)
			flag1[j] = true;
	}
	for (int i = 0; i < a2; i++) {
		int from, to;
		cin >> from >> to;
		for (int j = from; j < to; j++)
			flag2[j] = true;
	}
	int res1 = -1, res2 = -1;
	int opt, val;
	if (!flag1[0]) {
		memset(dp1, -1, sizeof dp1);
		memset(dp2, -1, sizeof dp2);
		set1(0, 1, 0);
		for (int i = 1; i < MAXN; i++) {
			if (!flag1[i]) {
				for (int offset = -MAXN; offset <= MAXN; offset++) {
					opt = -1;
					val = get1(i - 1, offset - 1);
					if (val != -1) {
						if (opt == -1 || val < opt)
							opt = val;
					}
					val = get2(i - 1, offset - 1);
					if (val != -1) {
						if (opt == -1 || val + 1 < opt)
							opt = val + 1;
					}
					if (opt != -1)
						set1(i, offset, opt);
				}
			}
			if (!flag2[i]) {
				for (int offset = -MAXN; offset <= MAXN; offset++) {
					opt = -1;
					val = get2(i - 1, offset + 1);
					if (val != -1) {
						if (opt == -1 || val < opt)
							opt = val;
					}
					val = get1(i - 1, offset + 1);
					if (val != -1) {
						if (opt == -1 || val + 1 < opt)
							opt = val + 1;
					}
					if (opt != -1)
						set2(i, offset, opt);
				}
			}
		}
		val = get1(MAXN - 1, 0);
		if (val != -1) {
			if (res1 == -1 || val < res1)
				res1 = val;
		}
		val = get2(MAXN - 1, 0);
		if (val != -1) {
			if (res1 == -1 || val + 1 < res1)
				res1 = val + 1;
		}
	}
	if (!flag2[0]) {
		memset(dp1, -1, sizeof dp1);
		memset(dp2, -1, sizeof dp2);
		set2(0, -1, 0);
		for (int i = 1; i < MAXN; i++) {
			if (!flag1[i]) {
				for (int offset = -MAXN; offset <= MAXN; offset++) {
					opt = -1;
					val = get1(i - 1, offset - 1);
					if (val != -1) {
						if (opt == -1 || val < opt)
							opt = val;
					}
					val = get2(i - 1, offset - 1);
					if (val != -1) {
						if (opt == -1 || val + 1 < opt)
							opt = val + 1;
					}
					if (opt != -1)
						set1(i, offset, opt);
				}
			}
			if (!flag2[i]) {
				for (int offset = -MAXN; offset <= MAXN; offset++) {
					opt = -1;
					val = get2(i - 1, offset + 1);
					if (val != -1) {
						if (opt == -1 || val < opt)
							opt = val;
					}
					val = get1(i - 1, offset + 1);
					if (val != -1) {
						if (opt == -1 || val + 1 < opt)
							opt = val + 1;
					}
					if (opt != -1)
						set2(i, offset, opt);
				}
			}
		}
		val = get2(MAXN - 1, 0);
		if (val != -1) {
			if (res2 == -1 || val < res2)
				res2 = val;
		}
		val = get1(MAXN - 1, 0);
		if (val != -1) {
			if (res2 == -1 || val + 1 < res2)
				res2 = val + 1;
		}
	}
	if (res1 != -1 && res2 != -1)
		cout << min(res1, res2) << endl;
	else if (res1 != -1)
		cout << res1 << endl;
	else
		cout << res2 << endl;
}

int main() {
	int t, i;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
