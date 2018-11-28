#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <limits.h>
#include <math.h>
#include <unordered_map>
#include <assert.h>
using namespace std;

#define ran(i, a, b) for ((i) = (a); (i) < (b); (i)++)
#define rep(i, a) ran ((i), 0, (a))
#define rep1(i, a) ran ((i), 1, (a)+1)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef unsigned long long ull;
#define _0 first
#define _1 second
#define _pb(x) push_back(x)
#define _mp(x, y) make_pair(x, y)
#if defined(SHIROKO1_LOCAL) && !defined(NDEBUG)
#define DEBUG(...) fprintf(stderr, "[DEBUG] " __VA_ARGS__)
#else
#define DEBUG(...) ((void)0)
#endif

int main()
{
	int taskc;
	cin >> taskc;
	int taski;
	rep1 (taski, taskc) {
		int n;
		long double d;
		cin >> d >> n;
		int i;
		long double mt = 0;
		rep (i, n) {
			long double k, s;
			cin >> k >> s;
			auto m = (d-k)/s;
			mt = max(m, mt);
		}
		printf("Case #%i: %.8lf\n", taski, (double)(d/mt));
	}
	return 0;
}
