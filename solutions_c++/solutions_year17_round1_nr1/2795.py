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

int n, m;

string ss[33];

int go(string *st) {
	string s[33];
	int l[33], r[33], d[33], t[33];
	forn(i, n)
		s[i] = st[i];

	while (1) {
		int qf = 0;
		forn(c, 26)
			l[c] = t[c] = 55, r[c] = d[c] = -1;
		forn(i, n)
			forn(j, m) {
				if (s[i][j] == '?')
					qf = 1;
				else {
					int c = s[i][j] - 'A';
					l[c] = min(l[c], i);
					r[c] = max(r[c], i);
					t[c] = min(t[c], j);
					d[c] = max(d[c], j);
				}
			}
		if (!qf)
			break;
		//forn(c, 26)
		//	if (r[c] >= 0)
		//		cerr << ((char)('A' + c)) << ": " << "l = " << l[c] << " r = " << r[c] << " t = " << t[c] << " d = " << d[c] << endl;
		int sf = 0;
		//cerr << "before\n";
		forn(i, n)
			forn(j, m)
				if (s[i][j] == '?') {
					int fc = -1;
					forn(c, 26)
						if (l[c] <= i && i <= r[c] && t[c] <= j && j <= d[c]) {
							//cerr << "simple paint\n";
							s[i][j] = (char)('A' + c);
							fc = c;
							break;
						}
					if (fc >= 0)
						sf = 1;
				}
		//cerr << "after\n";
		int did = 0;
		forn(c, 26) {
			if (r[c] == -1)
				continue;
			int ok;
			// to the left
			if (l[c] > 0) {
				ok = 0;
				for(int j = t[c]; j <= d[c]; ++j)
					if (s[l[c] - 1][j] != '?') 
						ok = 1;
				if (!ok) {
					did = 1;
					//cerr << "paiting " << ((char)('A'+c)) << ": I = " << (l[c] - 1) << ", j = " << "(" << t[c] << ", " << d[c] << ")\n";
					for(int j = t[c]; j <= d[c]; ++j)
						s[l[c] - 1][j] = (char)('A' + c);
					if (go(s))
						return true;
					for(int j = t[c]; j <= d[c]; ++j)
						s[l[c] - 1][j] = '?';
				}
			}
			// to the right
			if (r[c] < n - 1) {
				ok = 0;
				for(int j = t[c]; j <= d[c]; ++j)
					if (s[r[c] + 1][j] != '?') 
						ok = 1;
				if (!ok) {
					did = 1;
					//cerr << "paiting " << ((char)('A'+c)) << ": I = " << (r[c] + 1) << ", j = " << "(" << t[c] << ", " << d[c] << ")\n";
					for(int j = t[c]; j <= d[c]; ++j)
						s[r[c] + 1][j] = (char)('A' + c);
					if (go(s))
						return true;
					for(int j = t[c]; j <= d[c]; ++j)
						s[r[c] + 1][j] = '?';
				}
			}
			// to the up
			if (t[c] > 0) {
				ok = 0;
				for(int j = l[c]; j <= r[c]; ++j)
					if (s[j][t[c] - 1] != '?') 
						ok = 1;
				if (!ok) {
					did = 1;
					//cerr << "paiting " << ((char)('A'+c)) << ": J = " << (t[c] - 1) << ", i = " << "(" << l[c] << ", " << r[c] << ")\n";
					for(int j = l[c]; j <= r[c]; ++j)
						s[j][t[c] - 1] = (char)('A' + c);
					if (go(s))
						return true;
					for(int j = l[c]; j <= r[c]; ++j)
						s[j][t[c] - 1] = '?';
				}
			}
			// to the down
			if (d[c] < m - 1) {
				ok = 0;
				for(int j = l[c]; j <= r[c]; ++j)
					if (s[j][d[c] + 1] != '?') 
						ok = 1;
				if (!ok) {
					did = 1;
					//cerr << "paiting " << ((char)('A'+c)) << ": J = " << (d[c] + 1) << ", i = " << "(" << l[c] << ", " << r[c] << ")\n";
					for(int j = l[c]; j <= r[c]; ++j)
						s[j][d[c] + 1] = (char)('A' + c);
					if (go(s))
						return true;
					for(int j = l[c]; j <= r[c]; ++j)
						s[j][d[c] + 1] = '?';
				}
			}
		}
		if ((!did) && sf == 0) {
			return NULL;
		}
	}
	forn(i, n)
		forn(j, m)
			ss[i][j] = s[i][j];
	return true;
}


void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;
	forn(ttt, tc) {
		cerr << (ttt + 1) << endl;
		if (ttt)
			puts("");
		printf("Case #%d: ", ttt + 1);
		cin >> n >> m;
		cerr<< n << " " << m << endl;
		forn(i, n) {
			cin >> ss[i];
			cerr << ss[i] << endl;
		}

		go(ss);
		forn(i, n) {
			cout << "\n" << ss[i];
		}
	}
}