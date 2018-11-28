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

char in[30][30];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int N, M, i, j, k, l;
		scanf("%d %d", &N, &M);
		for (i = 0; i < N; i++) scanf("%s", in[i]);

		int st = 0;
		for (i = 0; i < N; i++) {
			vector <pair<char, int>> Vu;
			for (j = 0; j < M; j++) {
				if (in[i][j] == '?') continue;
				Vu.emplace_back(in[i][j], j);
			}
			if (Vu.empty()) continue;

			int p = 0;
			for (j = 0; j < Vu.size(); j++) {
				for (k = st; k <= i; k++) {
					for (l = p; l <= Vu[j].second; l++) {
						in[k][l] = Vu[j].first;
					}
				}
				p = Vu[j].second + 1;
			}
			for (j = st; j <= i; j++) for (k = p; k < M; k++) in[j][k] = Vu.back().first;
			st = i + 1;
		}
		for (j = st; j < N; j++) for (k = 0; k < M; k++) in[j][k] = in[j - 1][k];
		
		printf("Case #%d: \n", tc);
		for (i = 0; i < N; i++) printf("%s\n", in[i]);

		// Validate
		for (i = 0; i < 26; i++) {
			int sx = INF, sy = INF, ex = -INF, ey = -INF;
			for (j = 0; j < N; j++) {
				for (k = 0; k < M; k++) {
					if (in[j][k] != 'A' + i) continue;
					sx = min(sx, j);
					sy = min(sy, k);
					ex = max(ex, j);
					ey = max(ey, k);
				}
			}
			if (sx == INF) continue;
			for (j = sx; j <= ex; j++) {
				for (k = sy; k <= ey; k++) {
					if (in[j][k] != 'A' + i) {
						printf("ERR\n");
						exit(0);
					}
				}
			}
		}
		for (i = 0; i < N; i++) for (j = 0; j < M; j++) if (in[i][j] == '?') return !printf("ERR\n");
	}
	return 0;
}