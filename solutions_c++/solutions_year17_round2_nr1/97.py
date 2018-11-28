#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define FO(i, a, b) for (int i=(a); i<(b); i++)
#define FOR(i, n) FO(i, 0, n)

double solve(void)
{
	int d, n;
	cin >> d >> n;
	double maxt = 0;
	FOR(i, n){
		double k, s;
		cin >> k >> s;
		double t = (d - k) / s;
		maxt = max(maxt, t);
	}

	return d / maxt;
}

int main(void)
{
	int t;
	ios::sync_with_stdio(false);
	cin >> t;
	FOR(i, t)
		cout << "Case #" << i + 1 << ": " << fixed << setprecision(10) << solve() << '\n';
}
