#pragma region Include/Defines
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
#include <iostream>
#include <queue>

using namespace std;
typedef long long lli;
typedef vector<int> vi;
typedef vector<lli> vli;
typedef pair<int, int> pii;
typedef pair<lli, lli> pll;
typedef vector<pii> vpii;
typedef vector <pll> vpll;
typedef long double ld;

const int INF = 0x3f3f3f3f;
const lli LINF = 0x3f3f3f3f3f3f3f3f;

template<typename T, typename T2> inline void _max(T &a, T2 b) { a = max((T)a, (T)b); }
template<typename T, typename T2> inline void _min(T &a, T2 b) { a = min((T)a, (T)b); }

#ifdef _DEBUG
#define epr(...) fprintf(stderr,__VA_ARGS__)
#else
#define epr(...) 
#endif
#pragma endregion

const int MAX = 105;
int n, p, a[MAX];
int rem[5] = { 0 };
int dp[MAX][MAX][MAX] = { 0 };
vector<map<int, int>> steps;
map<int, int> tmp;

void clear() {
	memset(dp, -1, sizeof(dp));
	memset(rem, 0, sizeof(rem));
	steps.clear();
	tmp.clear();
}

void read() {
	scanf("%d%d", &n, &p);
	for (int i = 0; i < n; i++) scanf("%d", &a[i]);
}


int sum;
void gen(int cur) {
	if (cur == p) {
		if (sum && sum % p == 0) steps.push_back(tmp);
		return;
	}
	for (int k = 0; k < p; k++) {
		tmp[cur] = k;
		sum += k * cur;
		gen(cur + 1);
		sum -= k * cur;
	}
}

int getDp(int r1, int r2, int r3) {
	if (r1 < 0 || r2 < 0 || r3 < 0) return 0;
	if (r1 == 0 && r2 == 0 && r3 == 0) return 0;
	if (dp[r1][r2][r3] == -1) {
		int res = 0;
		for (auto &step : steps) {
			int tres = 1 + getDp(r1 - step[1], r2 - step[2], r3 - step[3]);
			res = max(tres, res);
		}
		dp[r1][r2][r3] = res;
	}
	return dp[r1][r2][r3];
}



int solve() {
	for (int i = 0; i < n; i++) rem[a[i] % p]++;
	//if (p == 2) return rem[0] + (rem[1] + 1) / 2;
	sum = 0;
	for (int i = 1; i < 4; i++) tmp[i] = 0;
	gen(1);
	for (int i = 1; i < p; i++) {
		map<int, int> m;
		for (int j = 1; j < p; j++) if (i == j) m[j] = p; else m[j] = 0;
		steps.push_back(m);
	}
	int res = rem[0];
	int dpRes = getDp(rem[1], rem[2], rem[3]);
	res += dpRes;
	return res;
}

int main() {
#ifdef _LOCAL_VAN
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		clear();
		read();
		int res = solve();
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}