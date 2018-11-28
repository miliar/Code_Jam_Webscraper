
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>

#define PI 3.14159265358979323846 
#define PO << " " <<
#define P " "
#define ABS(x) (((x) > 0) ? (x) : (-(x)))
#define RND(x) ((int)( (x) + 0.5 ))
#define MAX(x, y) (( (x) > (y) ) ? (x) : (y))
#define MIN(x, y) (( (x) < (y) ) ? (x) : (y))
#define forn(i, ending) for (int i = 0; i < (ending); i++)
#define it(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long int lint;
typedef unsigned long long int ulint;
typedef std::pair <lint, lint> pint;
typedef vector <int> vi;
typedef vector <vi> vvi;

bool cmp(const pint& a, const pint& b) {
	return a.first * a.second < b.first * b.second;
}

int main() {
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int testn = 0;
	int t; cin >> t; 
	while (t--) {
		testn++;
		int n, k; 
		scanf("%d%d", &n, &k);
		vector <pint> hr(n);
		forn(i, n)
			scanf("%lld%lld", &hr[i].second, &hr[i].first);
		sort(it(hr), cmp);
		lint mx = 0;
		forn(i, n) {
			lint rnow = hr[i].second;
			int cnt = 0;
			lint hall = 0;
			for (int j = n - 1; j >= 0; j--)
				if (hr[j].second <= rnow && cnt < k && (j <= i || cnt + 1 < k)) {
					cnt++;
					hall += 2 * hr[j].second * hr[j].first;
				}
			if (cnt < k)
				continue;
			lint ths = rnow * rnow + hall;
			mx = max(ths, mx);
		}
		printf("Case #%d: ", testn);
		printf("%.9lf\n", (double)mx * PI);
	}
}

/*
1
10 4
3030 319412
11932 97
11261 33
3318 384301
3353 386249
3509 361181
3803 352504
3690 314852
3646 340821
10460 69

1
10 4

*/