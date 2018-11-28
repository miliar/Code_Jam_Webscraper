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
#define DBG 1
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
int N;
int R, O, Y, G, B, V;
string stable;

int solve_small()
{
    string first;
    stable = "";
    if (R > 0 && R >= Y && R >= B)
    {
        R--;
        first = "R";
    }
    else if (Y > 0 && Y >= R && Y >= B)
    {
        Y--;
        first = "Y";
    }
    else if (B > 0 && B >=R && B >= Y)
    {
        B--;
        first = "B";
    }
    else
        printf("something wrong to pick first, R:%d, Y:%d, B:%d\n", R, Y, B);
    stable += first;

    while (R + Y + B > 0)
    {
        if (stable[stable.size()-1] == 'R')
        {
            if (Y > 0 && (Y > B || (Y == B && first != "B")))
            {
                Y--;
                stable += "Y";
            }
            else if (B > 0 && (B > Y || (B == Y && first != "Y")))
            {
                B--;
                stable += "B";
            }
            else 
            {
                debug("IMPOSSIBLE!\n");
                debug("R:%d, Y:%d, B:%d\n", R, Y, B);
                debug("stable: %s\n", stable.c_str());
                return -1;
            }
        }
        else if (stable[stable.size()-1] == 'Y')
        {
            if (R > 0 && (R > B || (R == B && first != "B")))
            {
                R--;
                stable += "R";
            }
            else if (B > 0 && (B > R || (B == R && first != "R")))
            {
                B--;
                stable += "B";
            }
            else 
            {
                debug("IMPOSSIBLE!\n");
                debug("R:%d, Y:%d, B:%d\n", R, Y, B);
                debug("stable: %s\n", stable.c_str());
                return -1;
            }
        }
        else if (stable[stable.size()-1] == 'B')
        {
            if (Y > 0 && (Y > R || (Y == R && first != "R")))
            {
                Y--;
                stable += "Y";
            }
            else if (R > 0 && (R > Y || (R == Y && first != "Y")))
            {
                R--;
                stable += "R";
            }
            else 
            {
                debug("IMPOSSIBLE!\n");
                debug("R:%d, Y:%d, B:%d\n", R, Y, B);
                debug("stable: %s\n", stable.c_str());
                return -1;
            }
        }
        else if (R > 0 && stable[stable.size()-1] != 'R' && R > Y && R > B)
        {
            R--;
            stable += "R";
        }
        else if (Y > 0 && stable[stable.size()-1] != 'Y' && Y > R && Y > B)
        {
            Y--;
            stable += "Y";
        }
        else if (B > 0 && stable[stable.size()-1] != 'B' && B > R && B > Y)
        {
            B--;
            stable += "B";
        }
        else
        {
            debug("IMPOSSIBLE!\n");
            debug("R:%d, Y:%d, B:%d\n", R, Y, B);
            debug("stable: %s\n", stable.c_str());
            return -1;
        }
    }
    if (stable[0] == stable[stable.size()-1])
    {
        debug("IMPOSSIBLE!\n");
        debug("R:%d, Y:%d, B:%d\n", R, Y, B);
        debug("stable: %s\n", stable.c_str());
        return -1;
    }
    return 0;
}
int solve()
{
    return solve_small();
}

int main()
{
	int tt, T;

	cin >> T;
	
	for (tt = 1; tt <= T; ++tt)
	{
        cin >> N >> R >> O >> Y >> G >> B >> V;
        int res = solve();
        if (res == -1)
            printf("Case #%d: IMPOSSIBLE\n", tt);
        else
            printf("Case #%d: %s\n", tt, stable.c_str());
	}
	return 0;
}
