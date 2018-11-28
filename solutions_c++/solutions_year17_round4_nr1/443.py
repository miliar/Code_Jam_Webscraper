# define _CRT_SECURE_NO_WARNINGS
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional> 
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <bitset>
#include <string.h>
#include <stdio.h>
#include <limits.h>
#include <array>
#include <utility>
#include <memory>
#include <future>
#include <array>
//#include <unordered_map>

using namespace std;

#define STR(X) #X

#define ABS(a)      ((a>0)?(a):(-(a)))
#define MIN(a,b)    ((a<b)?(a):(b))
#define MAX(a,b)    ((a<b)?(b):(a))
#define FOR(i,a,n)    for ( int i = (a); i < (n); ++i)
#define FOR_(i,a,n)		for ( int i = (a); i >= (n); --i)
#define FORI(n)        for(int i = 0; i < n; ++i)
#define MEMS(a,b)    memset(a,b,sizeof(a))

#define MP(p1, p2)      std::make_pair(p1, p2)
#define RNG(container)  container.begin(), container.end()

using LD = long double;
using LL = long long;
using ULL = unsigned long long;
using UI = unsigned int;
using UC = unsigned char;
using VI = std::vector<int>;
using SI = std::set<int>;

using PI = std::pair<int, int>;
using PL = std::pair<LL, LL>;

constexpr LL		MOD = 1000000007;
constexpr double    EXP = 2.7182818284590452;
constexpr double    Pi = 3.141592653589793238463;
constexpr long double    EPS = 1e-4;
constexpr int		INF = 1000 * 1000 * 1001;
constexpr long long	INFL = (LL)INF * (LL)INF;

inline LL gcd(LL a, LL b)
{
    if (a < b) swap(a, b);

    while (b != 0)
    {
        a %= b;
        swap(a, b);
    }

    return a;
}

inline LL lcm(LL a, LL b)
{
    return (a / gcd(a, b)) * b;
}

LL extgcd(LL a, LL b, LL & x, LL & y)
{
    if (a == 0)
    {
        x = 0; y = 1;
        return b;
    }

    LL x11, y11;
    LL d = extgcd(b % a, a, x11, y11);
    x = y11 - (b / a) * x11;
    y = x11;
    return d;
}

 ULL poww(ULL v, ULL p, ULL mod)
{
    if (p == 0) return 1;

    if (p & 1)
    {
        return (poww(v, p - 1, mod) * v) % mod;
    }
    else
    {
        ULL t = poww(v, p / 2, mod);
        return (t * t) % mod;
    }
}

constexpr ULL L31018 = 3000000000000000000L;
constexpr ULL L1018 = 1000000000000000000L;

//////////////////
//////////////////

constexpr int MAXN = 102;

LL res = 0;

int n, p, a;

int step;
int t, x[4];
LL dp[MAXN][MAXN][MAXN][4];
int was[MAXN][MAXN][MAXN][4];

LL func(int x1, int x2, int x3, int r)
{	
	if(x1 == 0 && x2 == 0 && x3 == 0)
	{
		return 0;
	}
	
	if(was[x1][x2][x3][r] == step)
	{
		return dp[x1][x2][x3][r];
	}
	was[x1][x2][x3][r] = step;
	
	LL res = 0, tmp;
	
	if(x1 > 0)
	{
		tmp = r + 1;
		if(tmp >= p)
			tmp -= p;
		res = func(x1 - 1, x2, x3, tmp);
	}
	
	if(x2 > 0)
	{
		tmp = r + 2;
		if(tmp >= p)
			tmp -= p;
		tmp = func(x1, x2-1, x3, tmp);
		res = MAX(res, tmp);
	}
	
	if(x3 > 0)
	{
		tmp = r + 3;
		if(tmp >= p)
			tmp -= p;
		tmp = func(x1, x2, x3-1, tmp);
		res = MAX(res, tmp);
	}
	
	if(r == 0)
	{
		++res;
	}
	
	return dp[x1][x2][x3][r] = res;
}

void accept()
{
	cin >> t;
	
	FOR(i,1,t+1)
	{
		FOR(j,0,4)
		{		
			x[j] = 0;
		}
		
		scanf("%d%d", &n, &p);
		FOR(j,0,n)
		{
			scanf("%d", &a);		
			++x[a % p];
		}
		
		step = i;
		
		printf("Case #%d: %lld\n", i, func(x[1], x[2], x[3], 0) + x[0]);
	}
}

//		||
//		||
//     \||/
//    \\||//
//   \\\\////
//    \\\///
//     \\//
//      \/

int main(void)
{
	freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    accept();

    return 0;
}
