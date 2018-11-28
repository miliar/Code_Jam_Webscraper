#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef long long ll;

pair<ll, ll> run(ll n, ll k)
{
	ll lpart = n / 2 - (1 - n % 2);
	ll rpart = n / 2;
	if (k == 1)
		return make_pair(rpart, lpart);
	if (k % 2 == 0)
		return run(n % 2 == 1 ? lpart : rpart, k / 2);
	else
		return run(n % 2 == 0 ? lpart : rpart, k / 2);
}

void solve()
{
	ll n, k;
	cin >> n >> k;
	auto p = run(n, k);
	cout << p.first << ' ' << p.second << endl;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		solve();
	}
}