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
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int n, d;
		cin >> d >> n;
		double ti = 0;
		for (int i = 0; i < n; ++i) {
			cin >> k[i] >> s[i];
			ti = max(ti, 1.0 * (d - k[i]) / s[i]);
		}
		printf("Case #%d: %.8lf\n", t, d / ti);
	}
	return 0;
}
