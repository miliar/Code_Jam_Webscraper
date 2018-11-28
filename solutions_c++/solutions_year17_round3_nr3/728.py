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
	int N = in();
	int K = in();
	double U = fin();
	vector<double> P;
	fr(i, 0, N) {
		P.push_back(fin());
	}
	while (U > 0) {
		double minP = 2;
		fr(i, 0, N) {
			chmin(minP, P[i]);
		}
		double min2P = 2;
		fr(i, 0, N) {
			if (P[i] < min2P && P[i] > minP) {
				min2P = P[i];
			}
		}
		vector<int> ind;
		fr(i, 0, N) {
			if (abs(P[i] - minP) < 0.00000001) {
				ind.push_back(i);
			}
		}
		double sum = ind.size() * (min2P - minP);
		if (U >= sum) {
			U -= sum;
			fr(i, 0, ind.size()) {
				P[ind[i]] = min2P;
			}
		}
		else {
			double add = U / ind.size();
			fr(i, 0, ind.size()) {
				P[ind[i]] += add;
			}
			U = 0;
		}
	}
	double res = 1;
	fr(i, 0, N) {
		res *= P[i];
	}
	printf("%.9f\n", res);
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