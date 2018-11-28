#include "stdafx.h"
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
#include <array>
#include <list>
#include <stack>
#include <valarray>

using namespace std;

typedef unsigned uint;
typedef long long Int;
typedef unsigned long long UInt;

#define fr(i,a,b) for (int i = a; i < b; i++)
#define wh while(1)

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; scanf("%d", &x); return x; }
double fin() { double x; scanf("%lf", &x); return x; }
Int lin() { Int x; scanf("%lld", &x); return x; }

bool comp(pair<int, int> a, pair<int, int> b) {
	return a.first < b.first;
}

void solve() {
	int Ac = in();
	int Aj = in();
	vector<pair<int, int> > C, J;
	fr(i, 0, Ac) {
		int a = in();
		int b = in();
		C.push_back(pair<int, int>(a, b));
	}
	sort(C.begin(), C.end(), comp);
	fr(i, 0, Aj) {
		int a = in();
		int b = in();
		J.push_back(pair<int, int>(a, b));
	}
	sort(J.begin(), J.end(), comp);
	if ((Ac == 1 && Aj == 0) || (Ac == 0 && Aj == 1) || (Ac == 1 && Aj == 1)) {
		printf("%d\n", 2);
		return;
	}
	if (Ac == 2 && Aj == 0) {
		if (C[1].second - C[0].first <= 720 || C[0].second - C[1].first + 1440 <= 720) {
			printf("%d\n", 2);
			return;
		}
		else {
			printf("%d\n", 4);
			return;
		}
	}
	if (Ac == 0 && Aj == 2) {
		if (J[1].second - J[0].first <= 720 || J[0].second - J[1].first + 1440 <= 720) {
			printf("%d\n", 2);
			return;
		}
		else {
			printf("%d\n", 4);
			return;
		}
	}
}

int main() {
	ios::sync_with_stdio(false);

	int T = in();

	for (int CN = 1; CN <= T; ++CN) {
		printf("Case #%d: ", CN);
		solve();
	}

	return 0;
}