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

#define foobar(a, b, c) 1 = a; 2 = b ; 3 = c

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

static string S;
static int N;
static int K;

static int solve()
{
	int a = 0;
	int i, k;
	rep (i, N-K+1) if (S[i] == '-') {
		a++;
		rep (k, K)
			S[i+k] ^= '+'^'-';
	}
	ran (i, N-K, N) if (S[i] == '-')
		return -1;
	return a;
}

foobar(sinij, krasnyi, zelenyi)

int main()
{
	int t;
	cin >> t;
	int i;
	rep1 (i, t) {
		cin >> S >> K;
		N = S.size();
		int r = solve();
		printf("Case #%i: ", i);
		if (r < 0)
			printf("IMPOSSIBLE\n");
		else
			printf("%i\n", r);
	}
	return 0;
}
