#pragma warning(disable:4996)

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <iterator>
#include <random>
#include <time.h>
#include <tuple>
#include <functional>
#include <list>
#include <limits.h>
#define mp make_pair
#define ni(x) scanf("%d", &(x))
#define nii(x,y) scanf("%d%d",&(x),&(y))
#define mul(x,y) ((ll)(x)*(y)%mod)
#define mtp make_tuple
#define F(i,n) for(int i = 0; i < (n); i++)
#define FF(i,n) for(int i = 1; i <= (n); i++)
#define FE(i,n) for(int i = 0; i <= (n); i++)

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
const int mod = 1000000007;
const int inf = 2012345678;
const ll infl = 9012345678901234567;
const double pi = 3.1415926535897932384626433832795;
#ifndef __GNUG__
int __builtin_popcount(int n) {
	int c = 0;
	while (n) {
		n -= n&(-n); c++;
	}
	return c;
}
#endif
//----------------------------------------------------------------------------//


int main() {
#ifndef __GNUG__
	//freopen("input.txt", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; ni(T);
	while (T--) {
		static int casen = 0;
		printf("Case #%d: ", ++casen);
		ll n, k; scanf("%lld %lld", &n, &k);
		map<ll, ll> M;
		M[n] = 1;
		while (k > M.rbegin()->second) {
			k -= M.rbegin()->second;
			ll x = M.rbegin()->first;
			ll nm = M.rbegin()->second;
			M.erase(x);
			M[(x - 1) / 2] += nm;
			M[x / 2] += nm;
		}
		ll x = M.rbegin()->first;
		printf("%lld %lld\n", x / 2, (x - 1) / 2);
	}
	return 0;
}