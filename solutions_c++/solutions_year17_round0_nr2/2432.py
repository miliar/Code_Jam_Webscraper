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

ull p10[20];

int digsCount(ull n)
{
	int r = 0;
	while (n)
	{
		n /= 10;
		++r;
	}
	return r;
}

ull solve()
{
	ull n;
	cin >> n;
	int digs = digsCount(n);
	ull ans = p10[digs] / 9ull;
	if (ans > n)
		return p10[digs - 1] - 1ull;
	for (int i = digs - 1; i >= 0; --i)
	{
		ull w = p10[i + 1] / 9ull;
		while (ans + w <= n && ans % 10 < 9)
			ans += w;
	}
	return ans;
}

int main()
{
	p10[0] = 1;
	for (int i = 1; i < 20; ++i)
		p10[i] = p10[i - 1] * 10ull;
    ios::sync_with_stdio(false);

	int tt;
	cin >> tt;
	for (int i = 1; i <= tt; ++i)
	{
		cerr << i << "/" << tt << "\n";
		ull res = solve();
		cout << "Case #" << i << ": ";
		cout << res << "\n";
	}

    return 0;
}
