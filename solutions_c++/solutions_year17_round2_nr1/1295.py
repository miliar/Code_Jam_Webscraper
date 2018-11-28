#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

const ll INF = (sizeof(ll) == 8) ? 1e18 : 1e9;

void sol(ll cas)
{
	ll d, n;
	cin >> d >> n;
	vector <pair <ll, ll>> arr(n);
	ld t = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i].first >> arr[i].second;
		t = max(t, ld(d - arr[i].first) / ld(arr[i].second));
	}
	cout << "Case #" << cas << ": ";
	cout << fixed << setprecision(6) << (ld)d / t << endl;
}

int main()
{
	srand(time(0));
	ios::sync_with_stdio(0);
#ifdef _F1A4X_
	//ifstream cin("input.txt");
	//ofstream cout("output.txt");
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ll t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		sol(i + 1);
	}
#ifdef _F1A4X_
	cerr << endl << "\t" << clock() << " ms" << endl;
#endif
}