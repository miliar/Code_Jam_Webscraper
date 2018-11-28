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

const int MAX = 1e4;
char s[MAX];
int k;

void clear() {
}

void read() {
	scanf("%s%d", s, &k);
}

void solve(int t) {
	int n = strlen(s);
	int res = 0;
	for (int i = 0; i < n - k + 1; i++)
		if (s[i] == '-') {
			for (int j = 0; j < k; j++) s[i + j] = s[i + j] == '-' ? '+' : '-';
			res++;
		}
	bool possible = true;
	for (int i = n - k + 1; i < n; i++) possible &= s[i] == '+';
	printf("Case #%d: ", t);
	if (!possible) printf("IMPOSSIBLE\n");
	else printf("%d\n", res);
}

int main() {
#ifdef _LOCAL_VAN
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
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