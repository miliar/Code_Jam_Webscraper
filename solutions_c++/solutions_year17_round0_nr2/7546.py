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

int t;
string s;

bool isValid(string num)
{
	bool res = true;
	int len = num.length();
	
	FOR(i,1,len)
	{
		if(num[i] < num[i-1])
		{
			res = false;
			break;
		}
	}
	
	return res;
}

void set_9(string& num, int b)
{
	int len = num.length();
	
	FOR(i,b,len)
	{
		num[i] = '9';
	}
}

int len = 0;

void accept()
{
	cin >> t;
	FOR(j,0,t)
   	{
		cin >> s;
		len = s.length();
		
		for(int i = len - 1; i > 0; --i)
		{
			if(s[i] < s[i-1])
			{
				--s[i-1];					
				set_9(s, i);
			}
		}
		
		if(s[0] == '0')
		{		
			printf("Case #%d: %s\n", j + 1, s.c_str() + 1);
		}
		else
		{
			printf("Case #%d: %s\n", j + 1, s.c_str());
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
    freopen("B-large.in", "r", stdin);
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
