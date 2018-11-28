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

char b[30][30];
int main() {
#ifndef __GNUG__
	//freopen("input.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; ni(T);
	while (T--) {
		static int casen = 0;
		printf("Case #%d: ", ++casen);
		puts("");
		int n, m; nii(n, m);
		F(i, n)scanf("%s", b[i]);
		int fi = -1;
		F(i, n) {
			int l = 0;
			F(j, m) {
				if (b[i][j] != '?') {
					for (int k = l; k < j; k++) {
						b[i][k] = b[i][j];
					}
					l = j + 1;
				}
			}
			if (l == 0) {
				if (fi != -1) {
					F(j, m)b[i][j] = b[i - 1][j];
				}
				continue;
			}
			if (fi == -1)fi = i;
			F(j, m) {
				if (b[i][j] == '?')b[i][j] = b[i][l - 1];
			}
		}
		F(i, n) {
			if (b[i][0] != '?')continue;
			F(j, m)b[i][j] = b[fi][j];
		}
		F(i, n) {
			printf("%s\n", b[i]);
		}
	}
	
}