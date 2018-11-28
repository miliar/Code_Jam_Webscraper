#include "stdio.h"
//#include "string.h"
#include "string"
#include "math.h"
#include "set"
#include "map"
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
int N, D;
double K[1024], S[1024];

double solve()
{
    double slowest = -1;
    for (int i = 0; i < N; ++i)
        slowest = MAX(slowest, (double)(D-K[i]) / S[i]);

    return D / slowest;
}

int main()
{
	int tt, T;

	cin >> T;
	
	for (tt = 1; tt <= T; ++tt)
	{
        cin >> D >> N;
        for (int i = 0; i< N; ++i)
            cin >> K[i] >> S[i];
		printf("Case #%d: %06f\n", tt, solve());
	}
	return 0;
}
