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

#define ABS(a)      ((a>0)?a:-(a))
#define MIN(a,b)    ((a<b)?(a):(b))
#define MAX(a,b)    ((a<b)?(b):(a))
#define FOR(i,a,n)    for ( int i = (a); i < (n); ++i)
#define FOR_(i,a,n)		for ( int i = (a); i >= (n); --i)
#define FORI(n)        for(int i = 0; i < n; ++i)
#define MEMS(a,b)    memset(a,b,sizeof(a))

#define MP(p1, p2)      std::make_pair(p1, p2)
#define RNG(container)  container.begin(), container.end()

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
constexpr double    Pi = 3.1415926535;
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

constexpr int MAXN = 100005;

int t, k, len;
string s;
int res = 0;

void swap_s(int l, int r)
{
	FOR(i,l,r)
	{
		if(s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';	
	}
}

void accept()
{
	cin >> t;
	FOR(j,0,t)
   	{
   		res = 0;
		cin >> s >> k;
		len = s.length();
		FOR(i,0,len-k+1)
		{
			if(s[i] == '-')
			{
				swap_s(i, i + k);
				++res;
			}
		}
		
		FOR(i,len-k+1,len)
		{
			if(s[i] == '-')
			{
				res = -1;
				break;
			}				
		}
		
		if(res >= 0)
		{
			printf("Case #%d: %d\n", j + 1, res);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", j + 1);
		}
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

#ifdef _DEBUG
//    LL startTime = clock();
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    //	freopen("I.in", "r", stdin);
    //	freopen("cinema.out", "w", stdout);
#endif

    accept();
    //	build();

//#if Debug
//    //	printf("\n\n\t TIME: %.5lf", double((clock() - startTime)) / 1000.0f); /// CLOCKS_PER_SEC));
//    int l;
//    cin >> l;
//#endif
    return 0;
}
