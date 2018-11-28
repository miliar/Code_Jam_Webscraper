#define _CRT_SECURE_NO_WARNINGS
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


void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;
	forn(ttt, tc) {
		printf("Case #%d: ", ttt + 1);
		int n, k;
		ld u, p[123];
		cin >> n >> k >> u;
		forn(i, n) {
			cin >> p[i];
		}
		p[n] = 1.;
		while (u > 1e-9) {
			sort(p, p + n);
			int i = 1;
			while (i <= n && fabsl(p[0] - p[i]) < 1e-9)
				++i;
			if (i <= n) {
				ld val = min(p[i] - p[0], u / i);
				//cerr << "adding " << val << " to first " << i << " cores\n";
				forn(j, i)
					p[j] += val;
				u -= val * i;
			} else
				break;
		}
		ld res = 1.;
		forn(i, n) {
			res *= p[i];
		}
		printf("%.12llf\n", res);
	}
}