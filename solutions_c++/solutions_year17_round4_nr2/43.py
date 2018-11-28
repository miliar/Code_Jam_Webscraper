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

vector <int> Vin[1050];
int cnt[1050];
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int N, C, M, i;
		scanf("%d %d %d", &N, &C, &M);
		for (i = 1; i <= M; i++) {
			int t1, t2;
			scanf("%d %d", &t1, &t2);
			Vin[t2].push_back(t1);
			cnt[t1]++;
		}

		ll st = 0, en = INF, mi, rv = en + 1, a = 0;
		for (i = 1; i <= C; i++) st = max(st, (ll)Vin[i].size());
		while (st <= en) {
			mi = (st + en) / 2;
			ll c = 0, x = 0;
			for (i = 1; i <= N; i++) {
				if (cnt[i] <= mi) {
					c += mi - cnt[i];
					continue;
				}
				else {
					if (c < cnt[i] - mi) break;
					c -= cnt[i] - mi;
					x += cnt[i] - mi;
					continue;
				}
			}
			if (i > N) {
				rv = mi, a = x;
				en = mi - 1;
			}
			else st = mi + 1;
		}
		printf("Case #%d: %lld %lld\n", tc, rv, a);
		for (i = 1; i <= C; i++) Vin[i].clear();
		for (i = 1; i <= N; i++) cnt[i] = 0;
	}
	return 0;
}