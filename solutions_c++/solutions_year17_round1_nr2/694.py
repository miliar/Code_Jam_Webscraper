#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <functional>
#include <cassert>
#include <map>
#include <set>
#include <list>

using namespace std;
typedef long long lli;
typedef vector<int> vi;
typedef vector<lli> vli;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef long double ld;

const int INF = 0x3f3f3f3f;
const lli LINF = 0x3f3f3f3f3f3f3f3f;

//#define _LOCAL_DEBUG_
#ifdef _LOCAL_DEBUG_
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...) 
#endif

const int MAX = 60;
const int MAXSERV = 1e6 + 10;
int nPack, nIng;
int g[MAX] = { 0 };
int p[MAX][MAX] = { 0 };
set<pii> s[MAX];
pii b[MAX][MAX];

void clear() {
	for (int i = 0; i < MAX; i++) s[i].clear();
}

void read() {
	scanf("%d%d", &nIng, &nPack);
	for (int i = 0; i < nIng; i++) scanf("%d", &g[i]);
	for (int i = 0; i < nIng; i++)
		for (int j = 0; j < nPack; j++)
			scanf("%d", &p[i][j]);
	for (int i = 0; i < nIng; i++) sort(p[i], p[i] + nPack);
}

void solve(int t) {
	
	set<int> starts;
	int u[MAX][MAX] = { 0 };

	for (int i = 0; i < nIng; i++) {;
		for (int j = 0; j < nPack; j++) {
			int tMin = 10 * p[i][j] / (11 * g[i]) + (10 * p[i][j] % (11 * g[i]) == 0 ? 0 : 1);
			int tMax = 10 * p[i][j] / (9 * g[i]);
			b[i][j].first = tMin, b[i][j].second = tMax;
			if (tMin <= tMax) starts.insert(tMin);
			else u[i][j] = 1;
		}
	}

	int res = 0;
	for(auto nServ : starts) {
		while (1) {
			bool found = true;
			for (int i = 0; i < nIng; i++) {
				bool ingFound = false;
				for (int j = 0; j < nPack; j++)
					if (!u[i][j] && b[i][j].first <= nServ && b[i][j].second >= nServ) {
						ingFound = true;
						break;
					}
				found &= ingFound;
			}
			if (found) {
				for (int i = 0; i < nIng; i++) {
					for (int j = 0; j < nPack; j++)
						if (!u[i][j] && b[i][j].first <= nServ && b[i][j].second >= nServ) {
							u[i][j] = 1;
							break;
						}
				}
				res++;
			}
			else break;
		}
	}

	printf("Case #%d: %d\n", t, res);
}

int main() {
#ifdef _LOCAL_VAN
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int it = 0; it < t; it++) {
		clear();
		read();
		solve(it + 1);
	}
	return 0;
}