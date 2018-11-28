#define _CRT_SECURE_NO_DEPRECATE
#include <functional>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <bitset>
#include <queue>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
/*--------------------------------*/
#define pb push_back
#define INT_MIN (1 << 31)
#define INT_MAX ~(1 << 31)
#define LL_MIN -9223372036854775808
#define LL_MAX  9223372036854775807
#define lower(c) char(32 | c)
#define upper(c) char(~32 & c)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define RFOR(i, a, b) for (int i = a; i >= b; i--)
#define FORIT(i, a, b) for (auto i = a; i != b; i++)
#define READ freopen("input.txt", "r", stdin);
#define WRITE freopen("output.txt", "w", stdout);
#define MOD ll(1000000007)
#define PI acos(-1)
/*-------------------------------------------------------------*/
#define IMP 10000

bitset<1000> all;
int n, sz;

void flip(int s, int e){ FOR(i, s, e) all.flip(i); }
bool check(){
	FOR(i, 0, sz - 1) if (!all[i]) return 0;
	return 1;
}

int solve(int i, int flips){
	if (check()) return flips;
	if (i > sz - n) return IMP;
	
	int ret1 = IMP, ret2 = IMP;
	if (!all[i]){
		flip(i, (i + n) - 1);
		ret1 = solve(i + 1, flips + 1);
		flip(i, (i + n) - 1);
	}
	else {
		ret2 = solve(i + 1, flips);
	}

	return min(ret1, ret2);
}

int main() {

	char c;
	int T;
	scanf("%d\n", &T);
	FOR(t, 1, T){
		all = 0;
		sz = 0;

		while (scanf("%c", &c) && c != ' ') all[sz++] = (c == '+');
		scanf("%d\n", &n);

		printf("Case #%d: ", t);
		int res = solve(0, 0);
		(res == IMP) ? printf("IMPOSSIBLE\n") : printf("%d\n", res);
	}

	return 0;
}