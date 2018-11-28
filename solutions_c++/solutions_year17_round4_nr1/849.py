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

int n, p, a[123];

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;
	forn(ttt, tc) {
		printf("Case #%d: ", ttt + 1);

		cin >> n >> p;
		int cnt[4];
		memset(cnt, 0, sizeof cnt);
		forn(i, n) {
			cin >> a[i];
			cnt[a[i] % p]++;
		}
		int res = cnt[0];
		if (p == 2)
			res += (cnt[1] + 1) / 2;
		else
			if (p == 3) {
				int com = min(cnt[1], cnt[2]);
				res += com;
				cnt[1] -= com;
				cnt[2] -= com;
				res += (cnt[1] + 2) / 3;
				res += (cnt[2] + 2) / 3;
			} else {
				// p == 4
				res += cnt[2] / 2;
				cnt[2] %= 2;
				int com = min(cnt[1], cnt[3]);
				res += com;
				cnt[1] -= com;
				cnt[3] -= com;

				cnt[1] += cnt[3];
				if (cnt[2]) {
					if (cnt[1] <= 2)
						res++;
					else {
						res++;
						cnt[1] -= 2;
						res += (cnt[1] + 3) / 4;
					}
				} else {
					res += (cnt[1] + 3) / 4;
				}
			}
		cout << res << endl;
	}
}