#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <set>
#include <algorithm>
#include <map>
#include <cmath>
#include <vector>
#include <queue>
#include <iomanip>
#include <string>

using namespace std;

typedef long long ll;

struct city
{
	long double power;
	long double speed;
	long double distToNextCity;
};

struct pony
{
	long double power;
	long double speed;
	long double time;
};

int d[105][105];
int u[105], v[105];

city a[105];

set<pony> st;
set<pony> tmp;

bool operator<(const pony& a, const pony& b)
{
	return a.time < b.time;
}

void solve()
{
	st.clear();
	tmp.clear();

	int n, q;
	cin >> n >> q;

	for (int i = 1; i <= n; i++) {
		cin >> a[i].power;
		cin >> a[i].speed;
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> d[i][j];
		}
	}

	for (int i = 1; i <= q; i++)
		cin >> u[i] >> v[i];

	for (int i = 1; i < n; i++)
		a[i].distToNextCity = d[i][i + 1];

	pony p;
	p.power = a[1].power - a[1].distToNextCity;
	p.speed = a[1].speed;
	p.time = a[1].distToNextCity / a[1].speed;
	st.insert(p);

	for (int i = 2; i < n; i++) {
		tmp.clear();

		long double bestTime = (*st.begin()).time;
		for (auto x : st) {
			if (x.power >= a[i].distToNextCity) {
				x.power -= a[i].distToNextCity;
				x.time += a[i].distToNextCity / x.speed;
				tmp.insert(x);
			}
		}
		if (a[i].power >= a[i].distToNextCity) {
			pony pTmp;
			pTmp.speed = a[i].speed;
			pTmp.power = a[i].power - a[i].distToNextCity;
			pTmp.time = bestTime + a[i].distToNextCity / a[i].speed;
			tmp.insert(pTmp);
		}

		swap(tmp, st);
	}

	cout << fixed << setprecision(7) << (*st.begin()).time << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ll TC;
	cin >> TC;
	for (ll i = 1; i <= TC; ++i) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}