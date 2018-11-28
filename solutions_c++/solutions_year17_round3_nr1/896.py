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

double pi = 3.1415926535897;
vector<int> R;
vector<pair<int, int> > H;
bool comp(pair<int, int> a, pair<int, int> b) {
	return 2 * pi * R[a.first] * a.second > 2 * pi * R[b.first] * b.second;
}

void solve() {
	int N = in();
	int K = in();
	R.clear();
	H.clear();
	double maxRes = 0;
	fr(i, 0, N) {
		R.push_back(in());
		H.push_back(pair<int, int>(i, in()));
	}
	sort(H.begin(), H.end(), comp);
	fr(j, 0, N) {
		int J = H[j].first;
		int maxR = R[J];
		double res = pi * maxR * maxR + 2 * pi * maxR * H[j].second;
		//printf("%.9f\n", res);
		int c = 1;
		fr(i, 0, N) {
			if (c == K) {
				break;
			}
			if (H[i].first != J && R[H[i].first] <= maxR) {
				c++;
				res += 2 * pi * R[H[i].first] * H[i].second;
				//printf("%.9f\n", res);
			}
		}
		//printf("FIN:%.9f\n", res);
		if (c == K) {
			chmax(maxRes, res);
		}
	}
	printf("%.9f\n", maxRes);
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