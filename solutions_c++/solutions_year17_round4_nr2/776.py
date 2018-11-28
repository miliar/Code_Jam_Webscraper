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

int n, c, m;
int b[1234], p[1234];

int took[1023];
int man[1023];

int promos;

int ok(int x) {
	memset(man, 0, sizeof man);
	memset(took, 0, sizeof took);
	promos = 0;
	forn(i, m) {
		if (man[b[i]] == x)
			return 0;
		int pl = p[i];
		while (pl >= 0 && took[pl] == x)
			pl--;
		if (pl < 0)
			return 0;
		if (pl != p[i])
			++promos;
		man[b[i]]++;
		took[pl]++;
	}
	return 1;
}

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;
	forn(ttt, tc) {
		printf("Case #%d: ", ttt + 1);

		cin >> n >> c >> m;
		cerr << (ttt + 1)  << ": " << n << " " << c << " " << m << endl;
		forn(i, m) {
			cin >> p[i] >> b[i];
			--b[i];
			--p[i];
		}

		int l = 1, r = m;
		int ans = m;
		while (l <= r) {
			int x = (l + r) >> 1;
			if (ok(x)) {
				r = x - 1;
				ans = x;
			} else
				l = x + 1;
		}
		ok(ans);
		cout << ans << " " << promos << endl;
	}
}