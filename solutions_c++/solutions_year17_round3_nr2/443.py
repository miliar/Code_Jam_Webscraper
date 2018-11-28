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

pair<int, pii> p[1234];

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;
	forn(ttt, tc) {
		printf("Case #%d: ", ttt + 1);
		cerr << (ttt + 1) << endl;
		int n, m, a[234], b[234];
		cin >> n >> m;
		forn(i, n + m) {
			cin >> a[i] >> b[i];
		}
		if (n == 1 && m == 0) {
			puts("2");
			continue;
		}
		if (n == 2 && m == 0) {
			int r = max(b[0], b[1]);
			int l = min(a[0], a[1]);
			if (r - l > 720 && max(a[0], a[1]) - min(b[0], b[1]) < 720)
				puts("4");
			else
				puts("2");
			continue;
		}
		if (n == 1 && m == 1) {
			puts("2");
			continue;
		}
		int mn = 1440;
		forn(i, n + m)
			mn = min(mn, a[i]);
		forn(i, n + m) {
			a[i] -= mn, b[i] -= mn;
		}
		forn(i, n + m)
			p[i] = mp(a[i], mp(b[i], i < n ? -1 : 1));
		
		int k = n + m;

		int have[3];
		int cnt[3];
		cnt[0] = cnt[2] = 0;
		have[0] = have[2] = 720;
		forn(i, k) {
			have[p[i].second.second + 1] -= p[i].second.first - p[i].first;
			++cnt[p[i].second.second + 1];
		}
		sort(p, p + k);

		while (1) {
			// find adj segments of a same type with a smallest dist between them
			int small = 100000;
			int idx = -1;
			forn(i, k) {
				int j = (i + 1) % k;
				if (p[i].second.second == p[j].second.second) {
					int l = p[i].second.first;
					int r = p[j].first;
					if (r < l)
						r += 1440;
					if (r - l < small && have[p[i].second.second + 1] >= r - l) {
						small = r - l;
						idx = i;
					}
				}
			}
			if (idx < 0)
				break;
			have[p[idx].second.second + 1] -= small;
			//cerr << "cnt: {" << cnt[0] << ", " << cnt[2] << "}\n";
			--cnt[p[idx].second.second + 1];
			if (idx < k - 1) {
				//cerr << "uniting (" << p[idx].first << ", " << p[idx].second.first << ") and " <<  "(" << p[idx + 1].first << ", " << p[idx + 1].second.first << ") of type " << (p[idx].second.second+1) << "\n";
				//cerr << "After that, cnt: {" << cnt[0] << ", " << cnt[2] << "}\n";
				p[idx].second = p[idx + 1].second;
				for(int i = idx + 1; i < k - 1; ++i)
					p[i] = p[i + 1];
				--k;
			} else {
				//cerr << "uniting (" << p[idx].first << ", " << p[idx].second.first << ") and " <<  "(" << p[0].first << ", " << p[0].second.first << ") of type " << (p[idx].second.second+1) << "\n";
				//cerr << "After that, cnt: {" << cnt[0] << ", " << cnt[2] << "}\n";
				p[idx].second.first = p[0].second.first + 1440;
				forn(i, k - 1)
					p[i] = p[i + 1];
				--k;
			}
		}
		forn(i, k) {
			int j = (i + 1) % k;
			if (p[i].second.second == p[j].second.second)
				++cnt[2 - p[i].second.second];
		}
		printf("%d\n", max(cnt[0], cnt[2]) * 2);
	}
}