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
char cake[25][25];
char direction[25][25];
int R, C;
void printCake()
{
    for (int r = 0; r < R; ++r)
    {
        for (int c = 0; c < C; ++c)
            cout << cake[r][c];
        cout << endl;
    }
}

int solve()
{
    int r, c;
    for (r = 0; r < R; ++r)
        for (c = 0; c < C; ++c)
            direction[r][c] = '?';
    
    for (r = 0; r < R; ++r)
    {
        for (c = 0; c < C; ++c)
        {
            if (cake[r][c] == '?')
            {
                if (c > 0 && cake[r][c-1] != '?')
                {
                    cake[r][c] = cake[r][c-1];
                    direction[r][c] = 'H';
                    direction[r][c-1] = 'H';
                }
                else
                {
                    int cc;
                    for (cc = c; cc < C && cake[r][cc] == '?'; ++cc);
                    if (cc < C)
                    {
                        direction[r][cc] = 'H';
                        // found initial on the right
                        for (; c < cc; ++c)
                        {
                            cake[r][c] = cake[r][cc];
                            direction[r][c] = 'H';
                        }
                        direction[r][cc] = 'H';
                    }
                }
            }
        }
    }

    for (r = 1; r < R; ++r) //skip first row
    {
        if (cake[r][0] != '?')
            continue;
        for (c = 0; c < C; ++c)
        {
            if (cake[r][c] != '?')
            {
                cake[r][c] = '@';
                debug("Something wrong at %d, %d\n", r, c);
            }
            cake[r][c] = cake[r-1][c];
        }
    }
    for (r = R-1; r >= 0; --r)
    {
        if (cake[r][0] != '?')
            continue;
        for (c = 0; c < C; ++c)
        {
            if (cake[r][c] != '?')
            {
                cake[r][c] = '@';
                debug("Something wrong at %d, %d\n", r, c);
            }
            cake[r][c] = cake[r+1][c];
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
        cin >> R >> C;
        for (int r = 0; r < R; ++r)
        {
            for (int c = 0; c < C; ++c)
                cin >> cake[r][c];
        }
        int res = solve();
		printf("Case #%d:\n", tt);
        printCake();
	}
	return 0;
}
