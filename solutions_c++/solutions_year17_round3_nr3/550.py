#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
#include <ctime>
#include <bitset>
#include <random>
using namespace std;

#pragma comment(linker, "/stack:64000000")

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

typedef vector<int> vi;
typedef vector<pair<int, int > > vii;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef vector<ld> vld;

typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef vector<vll> vvll;
typedef vector<vs> vvs;

typedef map<int, int> mpii;
typedef map<int, string> mpis;
typedef map<string, int> mpsi;
typedef map<string, string> mpss;

#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define sz(a) (int)((a).size())
#define len(a) (int)((a).length())

#define forr(i,n) for (int i = 0; i < (n); ++i)
#define fori(n) forr(i,n)
#define forj(n) forr(j,n)
#define fork(n) forr(k,n)
#define forin fori(n)
#define forjn forj(n)
#define forjm forj(m)
#define forkm fork(m)
#define foria(a) fori(sz(a))
#define foriv foria(v)
#define foris fori(len(s))
#define forja(a) forj(sz(a))
#define forjv forj(v)
#define forjs forj(len(s))

#define read cin>>
#define write cout<<
#define writeln write endl

#define readt int aaa; read aaa;
#define gett (bbb+1)
#define fort forr(bbb,aaa)


ld dis(ld x, ld y) { return sqrt(x*x + y*y); }
const ld PI = acos(ld(0.0)) * 2;

ll gcd(ll a, ll b) { return b ? gcd(b, a%b) : a; }

ld prob(const vld &v, int k)
{
	if (k < 0)
		return 0.0;

	vld dp(k + 1, 0);
	vld dp2(k + 1, 0);
	dp[0] = 1.0;
	for (auto p : v)
	{
		dp2 = dp;
		foria(dp2) dp2[i] *= (1.0 - p);
		foria(dp2) if (i + 1 != sz(dp2)) dp2[i + 1] += dp[i] * p;
		dp.swap(dp2);
	}
	return dp[k];
}

ld prob_atleast(const vld &v, int k)
{
	if (k == 0)
		return 1.0;

	vld dp(sz(v) + 1, 0);
	vld dp2(sz(v) + 1, 0);
	dp[0] = 1.0;
	for (auto p : v)
	{
		dp2 = dp;
		foria(dp2) dp2[i] *= (1.0 - p);
		foria(dp2) if (i + 1 != sz(dp2)) dp2[i + 1] += dp[i] * p;
		dp.swap(dp2);
	}
	ld result = 0;
	foria(dp) if (i >= k) result += dp[i];
	return result;
}


vld diffs(const vld &v, int k)
{
	int n = sz(v);
	vld result(n);
	forin
	{
		vld p2 = v;
		p2.erase(p2.begin() + i);
		result[i] = prob(p2, k - 1);
	}
	return result;
}

const ld EPS = 1e-5;

ld reeror(ld x, ld y)
{
	return fabs(y - x) / max(max(fabs(x), fabs(y)), ld(1e-20));
}

int main()
{
	ios::sync_with_stdio(false);

#ifdef _MSC_VER
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#else
#endif


	cout.setf(ios::fixed);
	cout.precision(20);

	readt;
	fort
	{
		int n, k;
		read n >> k;

		ld sum = 0;
		read sum;

		vld probs(n);
		for (auto& prob : probs)
			read prob;

		sort(all(probs));

		if (n == 1)
		{
			probs[0] += sum;
			sum = 0;
		}
		else
		{
			vector<int> picked(n, 0);
			vector<int> capped(n, 0);
			while (sum > 1e-8)
			{
				bool next = true;
				forin if (picked[i] && !capped[i] && fabs(probs[i] - 1) < 1e-8) capped[i] = true, next = false;

				auto d0 = diffs(probs, k);
				ld m0 = -1;
				int mndx = -1;
				foria(d0) if (!picked[i] && d0[i] > m0) { m0 = d0[i]; mndx = i; }
				if (next && mndx != -1)
					picked[mndx] = 1;

				int cnter = 0;
				forin if (picked[i] && !capped[i]) ++cnter;
				if (cnter == 0)
					break;

				ld maxv = 0;
				forin if (picked[i] && !capped[i]) maxv = max(maxv, probs[i]);

				ld step = sum / cnter * 1.5;
				ld cur = 0;
				forr(asf, 30)
				{
					step /= 2;
					auto test = min(cur + step, 1.0 - maxv);
					test = min(test, sum / cnter);
					auto ptest = probs;
					forin if (picked[i] && !capped[i]) ptest[i] += test;
					auto dtest = diffs(ptest, k);
					ld mtest = -1;
					int mndxtest = -1;
					foria(dtest) if (!picked[i] && dtest[i] > mtest) { mtest = dtest[i]; mndxtest = i; }

					auto x = *max_element(all(dtest));
					if (reeror(x, mtest) > 1e-8)
						cur = test;
				}
				cur += 1e-10;
				cur = min(cur, 1.0 - maxv);
				cur = min(cur, sum / cnter);
				forin if (picked[i] && !capped[i]) probs[i] += cur;
				sum -= cur * cnter;
			}
		}

		write "Case #" << gett << ": " << prob_atleast(probs, k);
		writeln;

		std::cout << gett << ' ' << sum << endl;
	}

	return 0;
}