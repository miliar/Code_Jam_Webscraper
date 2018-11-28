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

int solve()
{
	static char s[N];
	int n, k;
	scanf("%s%d", s, &k);
	n = strlen(s);
	int ans = 0;
	static bool flip[N];
	bool cflip = 0;
	memset(flip, 0, sizeof(flip));
	for (int i = 0; i < n; ++i)
	{
		cflip ^= flip[i];
		if (cflip)
			s[i] = (s[i] == '+' ? '-' : '+');
		if (s[i] == '-')
		{
			if (i + k > n)
				return -1;
			++ans;
			cflip ^= 1;
			flip[i + k] ^= 1;
		}
	}
	return ans;
}

int main()
{
    ios::sync_with_stdio(false);

	int tt;
	scanf("%d", &tt);
	for (int i = 1; i <= tt; ++i)
	{
		cerr << i << "/" << tt << "\n";
		int res = solve();
		cout << "Case #" << i << ": ";
		if (res == -1)
			cout << "IMPOSSIBLE\n";
		else
			cout << res << "\n";
	}

    return 0;
}
