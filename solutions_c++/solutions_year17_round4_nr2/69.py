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
//----------------------------------------------------------------------------//

vector<int> V[1000];
int d[1000];
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
		int n, c, m; nii(n, c); ni(m);
		F(i, c)d[i] = 0;
		F(i, n)V[i].clear();
		F(i, m) {
			int x, y; nii(y, x); x--; y--;
			V[y].push_back(x);
			d[x]++;
		}
		int M = *max_element(d, d + c);
		int to = 0;
		F(i, n) {
			to += V[i].size();
			M = max(M, (to + i) / (i + 1));
		}
		int x = 0;
		F(i, n) {
			if ((int)V[i].size() > M) {
				x += V[i].size() - M;
			}
		}
		printf("%d %d\n", M, x);
		fprintf(stderr, "Case %d complete\n", casen);
	}
	return 0;
}