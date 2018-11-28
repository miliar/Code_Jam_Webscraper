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

const string IMP = "IMPOSSIBLE";

string go(int c1, int c2, int c3, char x1, char x2, char x3)
{
	if (c1 == 0)
		return go(c2, c3, c1, x2, x3, x1);
	--c1;
	int c[] = {c1, c2, c3};
	char x[] = {x1, x2, x3};
	vector < vector < vector < int > > > d[3];
	d[0].assign(c1 + 1, vector<vector<int>>(c2 + 1, vector<int>(c3+1, 0)));
	d[1] = d[0];
	d[2] = d[0];
	d[0][0][0][0] = -1;
	int cc[3];
	for (cc[0] = 0; cc[0] <= c[0]; ++cc[0])
		for (cc[1] = 0; cc[1] <= c[1]; ++cc[1])
			for (cc[2] = 0; cc[2] <= c[2]; ++cc[2])
				for (int last = 0; last < 3; ++last)
				{
					if (cc[last] == 0)
						continue;
					int cj[3] = {cc[0], cc[1], cc[2]};
					--cj[last];
					for (int prev = 0; prev < 3; ++prev)
						if (prev != last && d[prev][cj[0]][cj[1]][cj[2]])
						{
							d[last][cc[0]][cc[1]][cc[2]] = prev + 1;
							break;
						}
				}
	
	cc[0] = c[0];
	cc[1] = c[1];
	cc[2] = c[2];
	int last;
	if (d[1][c1][c2][c3])
		last = 1;
	else if (d[2][c1][c2][c3])
		last = 2;
	else
		return IMP;
	string s;
	while (true)
	{
		s += x[last];
		int nlast = d[last][cc[0]][cc[1]][cc[2]] - 1;
		if (nlast == -2)
			break;
		--cc[last];
		last = nlast;
	}
	return s;
}

string solve()
{
	int nn;
	cin >> nn;
	int c1, c2, c3, cw1, cw2, cw3;
	cin >> c1 >> cw3 >> c2 >> cw1 >> c3 >> cw2;
	c1 -= cw1;
	c2 -= cw2;
	c3 -= cw3;
	if (c1 < 0 || c2 < 0 || c3 < 0)
		return IMP;
	
	if (c1 == 0 && cw1 != 0)
	{
		if (nn != cw1 * 2)
			return IMP;
		string s;
		for (int i = 0; i < cw1; ++i)
			s += "RG";
		return s;
	}
	if (c2 == 0 && cw2 != 0)
	{
		if (nn != cw2 * 2)
			return IMP;
		string s;
		for (int i = 0; i < cw2; ++i)
			s += "YV";
		return s;
	}
	if (c3 == 0 && cw3 != 0)
	{
		if (nn != cw3 * 2)
			return IMP;
		string s;
		for (int i = 0; i < cw3; ++i)
			s += "BO";
		return s;
	}

	string s = go(c1, c2, c3, 'R', 'Y', 'B');
	if (s == IMP)
		return IMP;
	
	for (int i = 0; i < sz(s); ++i)
		if (s[i] == 'R')
		{
			string w = s.substr(i, sz(s) - i);
			s = s.substr(0, i);
			for (int j = 0; j < cw1; ++j)
				s += "RG";
			s += w;
			break;
		}
	for (int i = 0; i < sz(s); ++i)
		if (s[i] == 'Y')
		{
			string w = s.substr(i, sz(s) - i);
			s = s.substr(0, i);
			for (int j = 0; j < cw2; ++j)
				s += "YV";
			s += w;
			break;
		}
	for (int i = 0; i < sz(s); ++i)
		if (s[i] == 'B')
		{
			string w = s.substr(i, sz(s) - i);
			s = s.substr(0, i);
			for (int j = 0; j < cw3; ++j)
				s += "BO";
			s += w;
			break;
		}
	return s;
}

int main()
{
    ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": " << solve() << "\n";
		cerr << i << " " << t << "\n";
	}

    return 0;
}
