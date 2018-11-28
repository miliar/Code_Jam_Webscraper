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

int r[50];
int it[50];

int main() {
#ifndef __GNUG__
	//freopen("input.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; ni(T);
	while (T--) {
		static int casen = 0;
		printf("Case #%d: ", ++casen);
		int n, p; nii(n, p);
		F(i, n)ni(r[i]);
		vector<vector<pii> > a(n);
		vector<int> V;
		F(i, n) {
			F(j, p) {
				int y; ni(y);
				int L = (10 * y + 11 * r[i] - 1) / (11 * r[i]);
				int R = 10 * y / (9 * r[i]);
				if (L <= R) {
					a[i].emplace_back(L, R);
					if (L > 0)V.push_back(L); 
					if (R > 0) V.push_back(R);
				}
			}
			sort(a[i].begin(), a[i].end());
		}
		sort(V.begin(), V.end());
		F(i, n)it[i] = 0;
		int ans = 0;
		for (auto &val : V) {
			bool pos = true;
			F(i, n) {
				while (it[i] < (int)a[i].size() && a[i][it[i]].second < val)it[i]++;
				if (it[i] >= (int)a[i].size() || a[i][it[i]].first > val)pos = false;
			}
			if (!pos)continue;
			ans++;
			F(i, n) {
				it[i]++;
			}
		}
		printf("%d\n", ans);
	}
	
}