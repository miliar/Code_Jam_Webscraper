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

char b[20];

bool incr(int X) {
	vector<int> V;
	while (X) {
		V.push_back(X % 10);
		X /= 10;
	}
	int sz = V.size();
	F(i, sz - 1)if (V[i] < V[i + 1]) return false;
	return true;
}

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
		scanf("%s", b);
		int X; sscanf(b, "%d", &X); int o = X;
		int n = strlen(b);
		F(i, n) {
			char c = b[i];
			bool good = false;
			bool bad = false;
			for (int j = i; j < n; j++) {
				if (b[j] > c) {
					good = true; break;
				}
				if (b[j] < c) {
					bad = true; break;
				}
			}
			if (bad) {
				b[i]--;
				for (int j = i + 1; j < n; j++)b[j] = '9';
				break;
			}
		}
		int i = 0;
		while (b[i] == '0')i++;
		printf("%s\n", b + i);
	}
	return 0;
}