/*
PROG: gcj3264486b
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
ll N;
set<ll> s;

void generate(ll x, int len)
{
//	cerr << x << ' ' << len << endl;
	if (len == 0)
	{
		s.insert(x);
		return;
	}
	int rem = x % 10;
	for (int j = rem; j < 10; j++)
	{
		generate(10 * x + j, len - 1);
	}
}

int32_t main()
{
	ios_base::sync_with_stdio(false);
	if (fopen("gcj3264486b.in", "r"))
	{	
		freopen ("gcj3264486b.in", "r", stdin);
		freopen ("gcj3264486b.out", "w", stdout);
	}
	for (int i = 0; i < 18; i++)
	{
		for (ll j = 1; j < 10; j++)
		{
			generate(j, i);
		}
	}
	s.insert(LLINF);
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cout << "Case #" << i << ": ";
		cin >> N;
		cout << *prev(s.upper_bound(N)) << '\n';
	}
	return 0;
}
