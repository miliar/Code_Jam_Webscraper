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

int k[1234], s[1234], d, n;

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;
	forn(ttt, tc) {
		cerr << (ttt + 1) << endl;
		//if (ttt)
		//	puts("");
		printf("Case #%d: ", ttt + 1);
		cin >> d >> n;
		forn(i, n) {
			cin >> k[i] >> s[i];
		}
		ld l = 0, r = 1e20, res = -1;
		forn(it, 300) {
			ld v = (l + r) * .5;
			ld t = d / v;
			bool ok = 1;
			forn(i, n) {
				ld dist = k[i] + t * s[i];
				if (dist < d){
					ok = 0;
					break;
				}
			}
			if (ok) {
				res = v;
				l = v;
			}else
				r = v;
		}
		printf("%.9llf\n", res);
	}
}