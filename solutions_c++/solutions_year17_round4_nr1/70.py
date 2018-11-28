#pragma warning(disable:4996)

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <iterator>
#include <random>
#include <time.h>
#include <tuple>
#include <functional>
#include <list>
#include <limits.h>
#define mp make_pair
#define ni(x) scanf("%d", &(x))
#define nii(x,y) scanf("%d%d",&(x),&(y))
#define mul(x,y) ((ll)(x)*(y)%mod)
#define mtp make_tuple
#define F(i,n) for(int i = 0; i < (n); i++)
#define FF(i,n) for(int i = 1; i <= (n); i++)
#define FE(i,n) for(int i = 0; i <= (n); i++)

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
const int mod = 1000000007;
const int inf = 2012345678;
const ll infl = 9012345678901234567;
const double pi = 3.1415926535897932384626433832795;
//----------------------------------------------------------------------------//


int cnt[4];

int main() {
#ifndef __GNUG__
	//freopen("input.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; ni(T);
	while (T--) {
		static int casen = 0;
		printf("Case #%d: ", ++casen);
		int n, p; nii(n, p);
		F(i, p)cnt[i] = 0;
		int tot = 0;
		F(i, n) {
			int x; ni(x);
			tot += x;
			cnt[x%p]++;
		}
		int ans = 0;
		ans += cnt[0];
		if (p == 2) {
			ans += cnt[1] / 2;
		}
		else if (p == 3) {
			ans += min(cnt[1], cnt[2]);
			int x = min(cnt[1], cnt[2]);
			cnt[1] -= x; cnt[2] -= x;
			ans += cnt[1] / 3;
			ans += cnt[2] / 3;
		}
		else if (p == 4) {
			ans += cnt[2] / 2;
			cnt[2] %= 2;
			ans += min(cnt[1], cnt[3]);
			int x = min(cnt[1], cnt[3]);
			cnt[1] -= x;
			cnt[3] -= x;
			if (cnt[2]) {
				if (cnt[3] > 1) {
					cnt[3] -= 2;
					ans++;
				}
				else if (cnt[1] > 1) {
					cnt[1] -= 2;
					ans++;
				}
			}
			ans += cnt[3] / 4;
			ans += cnt[1] / 4;
		}
		ans++;
		if (tot%p == 0)ans--;
		printf("%d\n", ans);
	}
	return 0;
}