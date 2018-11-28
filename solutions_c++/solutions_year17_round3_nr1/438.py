#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = (int)(a); i < (int)(b); ++i)
#define EPS 1E-9
#define INF 2000000000
#define ll long long
#define ld long double
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin(),a.end()
#define MAXN 100001
//#define PI (ld)3.1415926535897932384626433832795

int r[2134], h[1234];

pair<ld, int> p[1234];

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	int k, n;
	cin >> tc;
	forn(ttt, tc) {
		printf("Case #%d: ", ttt + 1);
		cerr << (ttt + 1) << endl;
		scanf("%d %d", &n, &k);
		forn(i, n) {
			scanf("%d %d", &r[i], &h[i]);
			p[i] = mp(M_PI * r[i] * 2. * h[i], r[i]);
		}

		ld best = -1;
		sort(p, p + n);
		reverse(p, p + n);

		forn(s, n) {
			ld res = 0;
			//int mxr = 0;
			//forn(i, k)
			//	if (mxr < p[i].second) {
			res = M_PI * p[s].second * 1. * p[s].second + p[s].first;
					//cerr << "r0 = " << p[0].second << ", RES = " << res << endl;
			//	}
			int tak = 1;

			forn(i, n) {
				if (tak == k)
					break;
				//cerr << "r = " << p[i].second << ", S = " << p[i].first << endl;
				if (i != s && p[i].second <= p[s].second)
					res += p[i].first, ++tak;
			}

			if (tak == k && res > best)
				best = res;
		}
		printf("%.12llf\n", best);
	}
}