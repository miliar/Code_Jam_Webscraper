/*
PROG: gcj3264486c_1
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

using namespace std;

typedef unsigned long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<int, long long> pil;
typedef pair<long long, int> pli;
typedef pair<long long, long long> pll;

int T;
ll N, K;

pll solve(ll cur, ll w)
{
//	cerr << cur << ' ' << w << endl;
	ll rt = (cur - 1)/2;
	ll lt = (cur - 1) - rt;
	if (w == 1ll)
	{
		return MP(lt, rt);
	}
	if (w % 2 == 0)
	{
		return solve(lt, w/2);
	}
	else
	{
		return solve(rt, w/2);
	}
}

int32_t main()
{
	ios_base::sync_with_stdio(false);
	if (fopen("gcj3264486c.in", "r"))
	{	
		freopen ("gcj3264486c.in", "r", stdin);
		freopen ("gcj3264486c.out", "w", stdout);
	}
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		cin >> N >> K;
		pll ans = solve(N, K);
		cout << ans.first << ' ' << ans.second << '\n';
	}
}
