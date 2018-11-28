#include "stdio.h"
#include "string.h"
#include "math.h"
#include "set"
#include "algorithm"
#include <iostream>
#include <gmpxx.h>

using namespace std;

/**************** debug ***************/
//#define DBG 1
#ifdef DBG
#define chkpoint(...) { fprintf(stderr, "[%s:%d]", __func__, __LINE__);fprintf(stderr, __VA_ARGS__); };
#define debug(...) { fprintf(stderr, __VA_ARGS__); };
#else
#define chkpoint(...) 
#define debug(...) 
#endif
/**************** debug ***************/

/**************** Useful macro ***************/
#define MIN(a, b) (((a)<(b))?(a):(b))
#define MAX(a, b) (((a)>(b))?(a):(b))
#define SET_MIN(a, b) a = MIN(a, b)
#define SET_MAX(a, b) a = MAX(a, b)
#define MPZ2STR(x) (x.get_str(10).c_str())
/**************** Useful macro ***************/
unsigned long long tidy(unsigned long long N)
{
    if (N<10)
        return 0;
    unsigned long long p = tidy(N/10);
    if (N%10 >= (N/10)%10)
        return p*10;
    else
        return p?p*10:1;
}

unsigned long long solve(unsigned long long N)
{
    for ( ; N > 0;)
    {
        debug("tidy(%llu): %llu\n", N, tidy(N));
        unsigned long long t = tidy(N);
        if (t == 0)
            return N;
        else if (t < 10)
            N-=1;
        else
        {
            t/=10;
            N = N/t*t - 1;
        }
    }
	return 0;
}

int main()
{
	int tt, T;

	cin >> T;
	
	for (tt = 1; tt <= T; ++tt)
	{
		unsigned long long N;
        cin >> N;
		printf("Case #%d: %lld\n", tt, solve(N));
	}
	return 0;
}
