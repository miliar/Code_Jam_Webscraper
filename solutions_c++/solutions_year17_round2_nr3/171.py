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

const int N = 111;

void solve()
{
	int n, q;
	cin >> n >> q;
	static int hdist[N], hspeed[N];
	for (int i = 0; i < n; ++i)
		cin >> hdist[i] >> hspeed[i];
	static ll d[N][N];
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			cin >> d[i][j];
			if (d[i][j] == -1)
				d[i][j] = LINF;
		}
		d[i][i] = 0;
	}

	for (int k = 0; k < n; ++k)
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
	
	static ld dt[N][N];
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			if (d[i][j] <= hdist[i])
				dt[i][j] = (ld)d[i][j] / hspeed[i];
			else
				dt[i][j] = DINF;

	for (int k = 0; k < n; ++k)
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				dt[i][j] = min(dt[i][j], dt[i][k] + dt[k][j]);
	
	for (int i = 0; i < q; ++i)
	{
		int x, y;
		cin >> x >> y;
		--x;
		--y;
		cout << " " << dt[x][y];
	}
}

int main()
{
    ios::sync_with_stdio(false);
	cout.precision(12);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ":";
		solve();
		cout << "\n";
		cerr << i << " " << t << "\n";
	}

    return 0;
}
