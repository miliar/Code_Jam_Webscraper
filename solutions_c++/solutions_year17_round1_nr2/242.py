/*
PROG: gcj5304486b
LANG: C++
 */
#include <cstdlib>
#include <csignal>
#include <csetjmp>
#include <cstdarg>
#include <typeinfo>
#include <bitset>
#include <functional>
#include <utility>
#include <ctime>
#include <cstddef>
#include <new>
#include <memory>
#include <climits>
#include <cfloat>
#include <limits>
#include <exception>
#include <cassert>
#include <cerrno>
#include <cctype>
#include <cwctype>
#include <cstring>
#include <cwchar>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <complex>
#include <valarray>
#include <numeric>
#include <iosfwd>
#include <ios>	
#include <istream>	
#include <ostream>
#include <iostream>
#include <fstream>	
#include <strstream>	
#include <iomanip>	
#include <streambuf>
#include <cstdio>
#include <locale>	
#include <clocale>

#define MP make_pair
#define PB push_back

#define SINF 10001
#define INF 1000000001
#define LLINF 1000000000000000001ll
#define EPS 0.000000000000001
#define PI ((4.0) * atan(1.0))
#define MAXN 55

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<int, long long> pil;
typedef pair<long long, int> pli;
typedef pair<long long, long long> pll;

int T;
int N, M;
ll arr[MAXN];
multiset<ll> s[MAXN];
ll K;
ll ans;

int32_t main()
{
	ios_base::sync_with_stdio(false);
	if (fopen("gcj5304486b.in", "r"))
	{	
		freopen ("gcj5304486b.in", "r", stdin);
		freopen ("gcj5304486b.out", "w", stdout);
	}
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		cin >> N >> M;
		for (int i = 0; i < N; i++)
		{
			s[i].clear();
		}
		ans = 0;
		for (int i = 0; i < N; i++)
		{
			cin >> arr[i];
		}
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				ll x;
				cin >> x;
				s[i].insert(x);
			}
		}
		while(!s[0].empty())
		{
			bool sol = false;
			ll u = *s[0].begin();
			ll lt = (u * 10)/11;
			if (u % 11)
			{
				lt++;
			}
			ll rt = (u * 10)/9;
			ll w = lt/arr[0];
			if (lt % arr[0])
			{
				w++;
			}
			if (w == 0)
			{
				w++;
			}
			ll z = rt/arr[0];
			if (w > z)
			{
				s[0].erase(s[0].begin());
				continue;
			}
			for (ll i = w; i <= z; i++)
			{
				bool sol = true;
				for (int j = 1; j < N; j++)
				{
					ll need = arr[j] * i;
					ll lf = (need * 9)/10;
					if (need % 10)
					{
						lf++;
					}
					ll rf = (need * 11)/10;
					auto x = s[j].lower_bound(lf);
					if (x == s[j].end() || *x > rf)
					{
						sol = false;
					}
				}
				if (sol)
				{
					for (int j = 1; j < N; j++)
					{
						ll need = arr[j] * i;
						ll lf = (need * 9)/10;
						if (need % 10)
						{
							lf++;
						}
						auto x = s[j].lower_bound(lf);
						s[j].erase(x);
					}
					ans++;
					break;
				}
			}
			s[0].erase(s[0].find(*s[0].begin()));
		}
		cout << ans << '\n';
		//grid[i][j] is the # of grams in the jth package of ith ingredient
	}
}
