#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef long long i64;
typedef __int128 i128;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < int > VI;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

int qq;

i64 go(int hd, int ad, int hk, int ak, int b, int d, int kd, int kb)
{
	int hd0 = hd;
	i64 ans = kd + kb;
	int z = 0;
	forn(i, kd)
	{
		if (++z > 1222) return 1e18;
		int ak0 = ak;
		ak -= d;
		if (ak < 0) ak = 0;
		hd -= ak;
		if (hd <= 0)
		{
			hd = hd0;
			ak = ak0;
			hd -= ak;
			if (hd <= 0) return 1e18;
			ans++;
			i--;
			continue;
//			if (hd <= 0) return 1e18;
		}
	}

	z = 0;
	forn(i, kb)
	{
		if (++z > 1222) return 1e18;
		hd -= ak;
		if (hd <= 0)
		{
			hd = hd0;
			hd -= ak;
			if (hd <= 0) return 1e18;
			ans++;
			i--;
			continue;
//			if (hd <= 0) return 1e18;
		}
		ad += b;
	}

	z = 0;
	while (hk > 0)
	{
		if (++z > 1222) return 1e18;
		ans++;
		if (hk <= ad) return ans;

		hd -= ak;
		if (hd <= 0)
		{
			hd = hd0;
			hd -= ak;
			if (hd <= 0) return 1e18;
			continue;
//			ans++;
//			if (hd <= 0) return 1e18;
		}
		else hk -= ad;
	}
	return ans;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &qq);
	forn(ii, qq)
	{
		printf("Case #%d: ", ii+1);
		fprintf(stderr, "Case #%d:\n", ii+1);
		
		int hd, ad, hk, ak, b, d;
		scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
		i64 ans = 1e18;
		forn(kd, 101)
		{
			forn(kb, 101)
			{
				i64 cur = go(hd, ad, hk, ak, b, d, kd, kb);
				if (cur < ans)
				{
//					cerr << kd << " " << kb << " " << cur << endl;
					ans = cur;
				}
			}
		}
		if (ans > 1e17) puts("IMPOSSIBLE");
		else printf("%lld\n", ans);
		
		fflush(stdout);
	}

	return 0;
}
