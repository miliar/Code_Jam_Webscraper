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
#define MAX_STALL 1000000
bool stall[MAX_STALL];
int Ls[MAX_STALL];
int Rs[MAX_STALL];
int max_minLsRs = -1;
int max_maxLsRs = -1;
int maxLsRs = -1;
int minLsRs = -1;

void solve(int N, int K)
{
    int i, j, k, l, r;
    int chosen;
    for (i = 0 ; i < MAX_STALL; ++i)
    {
        stall[i] = false;
        Ls[i] = -1;
        Rs[i] = -1;
    }
    maxLsRs = -1;
    minLsRs = -1;

    for (int k = 0; k < K; ++k)
    {
        // Calculate Ls
        for (l = 0; l < N; ++l)
        {
            if (stall[l])
                Ls[l] = -1;
            else
                Ls[l] = (l>0) ? Ls[l-1]+1 : 0;
        }

        // Calculate Rs
        for (r = N-1; r >= 0; --r)
        {
            if (stall[r])
                Rs[r] = -1;
            else
                Rs[r] = (r<N-1) ? Rs[r+1]+1 : 0;
        }

        max_minLsRs = -1;
        max_maxLsRs = -1;
        for (i = 0; i < N; ++i)
            max_minLsRs = MAX(max_minLsRs, MIN(Ls[i], Rs[i]));
        for (i = 0; i < N; ++i)
        {
            if (max_minLsRs == MIN(Ls[i], Rs[i]))
                max_maxLsRs = MAX(max_maxLsRs, MAX(Ls[i], Rs[i]));
        }
        
        chosen = -1;
        for (i = 0; i < N; ++i)
        {
            if (max_minLsRs == MIN(Ls[i], Rs[i]) &&
                    max_maxLsRs == MAX(Ls[i], Rs[i]))
            {
                chosen = i;
                stall[chosen] = true;
                debug("choose stall[%d]\n", chosen);
                break;
            }
        }
    }
    debug("last one chosen stall[%d]\n", chosen);
    minLsRs = MIN(Ls[chosen], Rs[chosen]);
    maxLsRs = MAX(Ls[chosen], Rs[chosen]);
}

int main()
{
	int tt, T;

	cin >> T;
	
	for (tt = 1; tt <= T; ++tt)
	{
		int N, K;
        cin >> N >> K;
        solve(N, K);
		printf("Case #%d: %d %d\n", tt, maxLsRs, minLsRs);
	}
	return 0;
}
