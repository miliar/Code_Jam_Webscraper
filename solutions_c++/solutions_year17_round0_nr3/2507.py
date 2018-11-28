#include <bits/stdc++.h>

#ifndef LOCAL
#define cerr dolor_sit_amet
#endif

#define mp make_pair
#define sz(x) ((int)((x).size()))
#define X first
#define Y second

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair < int , int > ipair;
typedef pair < ll , ll > lpair;
const int IINF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3fll;
const double DINF = numeric_limits<double>::infinity();
const ll MOD = 1000000007;
const double EPS = 1e-9;
const int DX[] = { 1,  0, -1,  0,  1, -1,  1, -1};
const int DY[] = { 0,  1,  0, -1,  1, -1, -1,  1};
ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }
ll sqr(ll x) { return x*x; } ll sqr(int x) { return (ll)x*x; }
double sqr(double x) { return x*x; } ld sqr(ld x) { return x*x; }

// ========================================================================= //

const int N = 1111;

lpair solve()
{
	ll n, k;
	cin >> n >> k;
	map < ll , ll > g;
	g[n] = 1;
	ll glen = 0;
	while (k > 0)
	{
		while (true)
		{
			auto it = prev(g.end());
			if (it->second == 0)
				g.erase(it);
			else
				break;
		}
		glen = g.rbegin()->first;
		ll gcnt = g.rbegin()->second;
		k -= gcnt;
		g.erase(glen);
		g[glen / 2] += gcnt;
		g[glen / 2 - (glen % 2 == 0)] += gcnt;
	}
	if (glen % 2 == 1)
		return {glen / 2, glen / 2};
	else
		return {glen / 2, glen / 2 - 1};
}

int main()
{
    ios::sync_with_stdio(false);

	int tt;
	cin >> tt;
	for (int i = 1; i <= tt; ++i)
	{
		cerr << i << "/" << tt << "\n";
		lpair res = solve();
		cout << "Case #" << i << ": ";
		cout << res.X << " " << res.Y << "\n";
	}

    return 0;
}
