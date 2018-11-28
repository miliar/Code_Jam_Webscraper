#include <stdio.h>  
#include <algorithm>  
#include <assert.h>  
#include <cmath>  
#include <complex>  
#include <deque>  
#include <functional>  
#include <iostream>  
#include <limits.h>  
#include <map>  
#include <math.h>  
#include <queue>  
#include <set>  
#include <stdlib.h>  
#include <string.h>  
#include <string>  
#include <time.h>  
#include <unordered_map>  
#include <unordered_set>  
#include <vector>  

#pragma warning(disable:4996)  
#pragma comment(linker, "/STACK:336777216")  
using namespace std;

#define mp make_pair  
#define Fi first  
#define Se second  
#define pb(x) push_back(x)  
#define szz(x) ((int)(x).size())  
#define rep(i, n) for(int i=0;i<n;i++)  
#define all(x) (x).begin(), (x).end()  
#define ldb ldouble  

typedef tuple<int, int, int> t3;
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
typedef long double ldb;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <ll, int> pli;
typedef pair <db, db> pdd;

int IT_MAX = 1 << 18;
const ll MOD = 1000000007;
const int INF = 0x3f3f3f3f;
const ll LL_INF = 0x3f3f3f3f3f3f3f3f;
const db PI = acos(-1);
const db ERR = 1E-11;

int dp3[105][105];
int dp[105][105][105];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, i, j, k, ii, jj, kk;

	dp[0][0][0] = 0;

	for (i = 0; i <= 100; i++) {
		for (j = 0; j <= 100; j++) {
			if (!i && !j) continue;
			for (ii = 0; ii <= 3 && ii <= i; ii++) {
				for (jj = 0; jj <= 3 && jj <= j; jj++) {
					if (ii == 0 && jj == 0) continue;
					if ((ii + jj * 2) % 3) continue;
					dp3[i][j] = max(dp3[i][j], dp3[i - ii][j - jj] + 1);
				}
			}
		}
	}

	for (i = 0; i <= 100; i++) {
		for (j = 0; j <= 100; j++) {
			for (k = 0; k <= 100; k++) {
				if (!i && !j && !k) continue;
				for (ii = 0; ii <= 4 && ii <= i; ii++) {
					for (jj = 0; jj <= 4 && jj <= j; jj++) {
						for (kk = 0; kk <= 4 && kk <= k; kk++) {
							if (ii == 0 && jj == 0 && kk == 0) continue;
							if ((ii + jj * 2 + kk * 3) % 4) continue;
							dp[i][j][k] = max(dp[i][j][k], dp[i-ii][j-jj][k-kk] + 1);
						}
					}
				}
			}
		}
	}
	

	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int N, P, t;
		int c[4] = { 0,0,0,0 };
		scanf("%d %d", &N, &P);
		for (i = 1; i <= N; i++) {
			scanf("%d", &t);
			c[t%P]++;
		}

		printf("Case #%d: ", tc);
		if (P == 2) {
			if (c[1] == 0) printf("%d\n", c[0]);
			else printf("%d\n", c[0] + (c[1] + 1) / 2);
		}
		if (P == 3) {
			if (c[1] == 0 && c[2] == 0) printf("%d\n", c[0]);
			else {
				int x = c[0] + 1;
				int v = 0;
				if (c[1]) v = max(v, dp3[c[1] - 1][c[2]]);
				if (c[2]) v = max(v, dp3[c[1]][c[2] - 1]);
				printf("%d\n", x + v);
			}
		}
		if (P == 4) {
			if (c[1] == 0 && c[2] == 0 && c[3] == 0) printf("%d\n", c[0]);
			else {
				int x = c[0] + 1;
				int v = 0;
				if(c[1]) v = max(v, dp[c[1] - 1][c[2]][c[3]]);
				if(c[2]) v = max(v, dp[c[1]][c[2] - 1][c[3]]);
				if(c[3]) v = max(v, dp[c[1]][c[2]][c[3] - 1]);
				printf("%d\n", x + v);
			}
		}
	}
	return 0;
}