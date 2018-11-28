
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
typedef std::pair <int, int> pint;
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
		int n, m; 
		scanf("%d%d", &n, &m);

		vector <pint> a(n), b(m);
		forn(i, n)
			scanf("%d%d", &a[i].first, &a[i].second);
		forn(i, m)
			scanf("%d%d", &b[i].first, &b[i].second);
		int night = 24 * 60;
		int day = night / 2;
		if (a.size() < b.size()) {
			swap(a, b);
			swap(n, m);
		}
		sort(it(a));
		int ans = -1;
		if (n + m == 1)
			ans = 2;
		else {
			if (n == 2) {
				if (a[1].second - a[0].first <= day || a[1].first - a[0].second >= day)
					ans = 2;
				else
					ans = 4;
			}
			else
				ans = 2;
		}
		
		printf("Case #%d: ", testn);
		printf("%d\n", ans);
	}
}

/*
3
1 1
540 600
840 900
2 0
900 1260
180 540
1 1
1439 1440
0 1

*/