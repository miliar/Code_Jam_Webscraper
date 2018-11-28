#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <iostream>
using namespace std;

long long dp[20][10][2];
int n;
int a[20];

long long sol (int ind, int l, int b) {
	if (ind == n) {
		return 0LL;
	}
	if (dp[ind][l][b] != -1) {
		return dp[ind][l][b];
	}

	long long ret = -2;
	long long base = 1LL;
	for (int i=1;i<n-ind;i++) {
		base *= 10LL;
	}

	long long res;
	for (long long i=l;i<10;i++) {
		if (b) {
			res = sol(ind+1, i, b);
		} else {
			if (i > a[ind]) {
				break;
			}
			res = sol(ind+1, i, i<a[ind]?1:0);
		}
		if (res != -2) {
			ret = max (ret, res + base*i);
		}
	}

	return dp[ind][l][b] = ret;
}

int main () {
	int t;
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	scanf ("%d", &t);

	for (int tc=1;tc<=t;tc++) {
		memset (dp, -1, sizeof(dp));
		long long x;
		scanf ("%lld", &x);
		n = 0;

		while (x) {
			a[n++] = x%10;
			x /= 10;
		}

		reverse (a, a+n);
		long long wc = 1LL;
		for (int i=1;i<n;i++) {
			wc *= 10LL;
		}
		wc --;
		printf ("Case #%d: %lld\n", tc, max(sol(0, 1, 0), wc));
	}

	return 0;
}