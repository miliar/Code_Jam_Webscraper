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
#define FN "contest"
//----------------------------------------------------------------------------//

int hd, ad, hk, ak, b, d;

int solve(int de, int bu) {
	int chd = hd;

	int cak = ak;
	bool hb = false;
	int ret = 0;
	int cn = 0;
	while (cn < de) {
		ret++;
		if (chd <= cak - d) {
			if (hb)return inf;
			hb = true;
			chd = hd;
		}
		else {
			hb = false;
			cak -= d;
			if (cak < 0)cak = 0;
			cn++;
		}
		chd -= cak;
		if (chd <= 0)return inf;
	}
	hb = false;
	int cad = ad;
	cn = 0;
	while (cn < bu) {
		ret++;
		if (chd <= cak) {
			if (hb)return inf;
			hb = true;
			chd = hd;
		}
		else {
			hb = false;
			cad += b;
			cn++;
		}
		chd -= cak;
		if (chd <= 0)return inf;
	}
	hb = false;
	int chk = hk;
	while (1) {
		ret++;
		if (cad >= chk) {
			break;
		}
		else if (chd <= cak) {
			if (hb)return inf;
			hb = true;
			chd = hd;
		}
		else {
			hb = false;
			chk -= cad;
		}
		chd -= cak;
		if (chd <= 0)return inf;
	}
	return ret;
}

//#define debug

int main() {
#ifndef __GNUG__
	//freopen("input.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);
	freopen("C-small-attempt2.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
#endif
	int T; ni(T);
	while (T--) {
		static int casen = 0;
		printf("Case #%d: ", ++casen); 
#ifdef debug
		puts("");
#endif
		nii(hd, ad); nii(hk, ak); nii(b, d);
		vector<int> V;
		FE(i, 100) {
			int x = inf;
			FE(j, 100) {
				int s = solve(i, j);
				x = min(x, s);
#ifdef debug
				printf("%d ", s);
#endif
			}
#ifdef debug
			puts("");
#endif
			V.push_back(x);
		}
#ifdef debug
		puts("FINAL"); 
		for (auto &x : V)printf("%d ", x); puts("");
#endif
#ifndef debug
		int ans = *min_element(V.begin(), V.end());
		if (ans == inf)puts("IMPOSSIBLE");
		else printf("%d\n", ans);
#endif
	}
	
}