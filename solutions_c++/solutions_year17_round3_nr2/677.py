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

constexpr LL		MOD = 1000000009;
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

constexpr int MAXN = 1450;

int t, Ac, Aj, l, r;
int res, tmp;
int step;

// -1 - none, 0 - first, 1 - second
int act[MAXN];
// [0 - first, 1 - second][time][first_time]
int dp[2][MAXN][MAXN / 2][2];
int was[2][MAXN][MAXN / 2][2];

int func(int cur, int time, int ftime, int fminute)
{	
	if(ftime > 720)
	{
		return INF;
	}
	
	if(time - ftime > 720)
	{
		return INF;
	}	
	
	if(act[time] == cur)
	{
		return INF;
	}
	
	if(was[cur][time][ftime][fminute] == step)
	{
		return dp[cur][time][ftime][fminute];
	}
	was[cur][time][ftime][fminute] = step;
	
	int res = 0, tmp = 0;
	
	if(time == 1440)
	{
		res = ((cur != fminute)?(1):(0));
	}
	else 
	{		
		int nxt = ((cur == 0)?(1):(0));
		int nxt_ftime = ((cur == 1)?(ftime + 1):(ftime));
		
		res = func(nxt, time + 1, nxt_ftime, fminute) + 1;
		tmp = func(cur, time + 1, nxt_ftime, fminute);	
		
		res = MIN(res, tmp);
	}
	
	return dp[cur][time][ftime][fminute] = res;
}

void accept()
{
	cin >> t;
	FOR(j,0,t)
	{
		step = j + 1;
		scanf("%d%d", &Ac, &Aj);
		
		FOR(i,0,MAXN)
		{
			act[i] = -1;
		}
		
		FOR(i,0,Ac)
		{
			scanf("%d%d", &l, &r);
			FOR(g,l,r)
			{
				act[g] = 0;
			}
		}
		
		FOR(i,0,Aj)
		{
			scanf("%d%d", &l, &r);
			FOR(g,l,r)
			{
				act[g] = 1;
			}
		}
		
		res = func(0, 0, 0, 0);
		tmp = func(1, 0, 0, 1);
		res = MIN(res, tmp);
		
		printf("Case #%d: %d\n", j+1, res);
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
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    accept();

    return 0;
}
