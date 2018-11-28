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

int IT_MAX = 1 << 17;
const ll MOD = 1000000007;
const int INF = 1034567891;
const ll LL_INF = 1234567890123456789ll;
const db PI = acos(-1);
const db ERR = 1E-11;

ll in[20];
ll ans[20];
bool isValid() {
	int i;
	for (i = 19; i >= 0; i--) if (in[i] != ans[i]) return in[i] > ans[i];
	return true;
}
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		ll N;
		scanf("%lld", &N);
		int i, j, k;
		for (i = 0; i < 20; i++, N /= 10) in[i] = N % 10;

		for (i = 19; i >= 0; i--) {
			for (j = 9; j >= 0; j--) {
				for (k = i; k >= 0; k--) ans[k] = j;
				if (isValid()) break;
			}
		}

		ll A = 0;
		for (i = 19; i >= 0; i--) A = A * 10 + ans[i];
		printf("Case #%d: %lld\n", tc, A);
	}
	return 0;
}