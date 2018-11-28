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

		int n, a, b, c, d, e, f;
		cin >> n >> a >> b >> c >> d >> e >> f;
		if (a > c + e || c > a + e || e > a + c) {
			puts("IMPOSSIBLE");
			continue;
		}
		string res = "";
		forn(i, n) {
			if (a >= c && a >= e) {
				if (!(i > 0 && res[i - 1] == 'R')) 
					res += "R", --a;
				else {
					if (c >= e)
						res += "Y", --c;
					else
						res += "B", --e;
				}
			} else
				if (c >= a && c >= e && !(i > 0 && res[i - 1] == 'Y'))
					res += "Y", --c;
				else
					if (e >= a && e >= c && !(i > 0 && res[i - 1] == 'B'))
						res += "B", --e;
					else
							if (c >= a && c >= e) {
								if (a >= e)
									res += "R", --a;
								else
									res += "B", --e;
							}
							else {
								if (c >= a)
									res += "Y", --c;
								else
									res += "R", --a;
							}
		}
		if (res.size() > 2 && res[0] == res[res.size() - 1]) {
			cerr << "Alarm test " << (ttt + 1) << endl;
			swap(res[res.size() - 1], res[res.size() - 2]);
		}
		cout << res << endl;
	}
}