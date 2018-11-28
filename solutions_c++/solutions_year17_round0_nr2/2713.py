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
	int t;
	cin >> t;
	int i;
	rep1 (i, t) {
		char S[32];
		cin >> S;
		int j, n, k;
		n = strlen(S);
		S[n] = 127;
		rep (k, 30) {
			rep (j, n) {
				if (S[j] > S[j+1]) {
					S[j++]--;
					break;
				}
			}
			ran (j, j, n)
				S[j] = '9';
		}
		S[n] = 0;
		rep (j, n-1) if (S[j] != '0')
			break;
		printf("Case #%i: %s\n", i, S+j);
	}
	return 0;
}
