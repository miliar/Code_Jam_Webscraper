#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
#include <bitset>		//UWAGA - w czasie kompilacji musi byc znany rozmiar wektora - nie mozna go zmienic
#include <cassert>
#include <iomanip>		//do setprecision
#include <ctime>
#include <complex>
using namespace std;

#define FOR(i,b,e) for(int i=(b);i<(e);++i)
#define FORQ(i,b,e) for(int i=(b);i<=(e);++i)
#define FORD(i,b,e) for(int i=(b)-1;i>=(e);--i)
#define REP(x, n) for(int x = 0; x < (n); ++x)

#define ST first
#define ND second
#define PB push_back
#define MP make_pair
#define LL long long
#define ULL unsigned LL
#define LD long double

const double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342;

const int MR = 1e3 + 10;

char s[MR];

int main()
{
    int T;
    scanf( "%d", &T );
    REP( c, T )
    {
        int K;
        scanf( "%s%d", s, &K );
        int n = strlen( s );
        int res = 0;
        REP( i, n - K + 1 )
        {
            if (s[i] == '-')
            {
                REP( j, K )
                {
                    if (s[j + i] == '-')
                        s[j + i] = '+';
                    else
                        s[j + i] = '-';
                }

                res++;
            }
        }

        bool bad = 0;

        REP( i, n )
            if (s[i] == '-')
                bad = 1;

        if (bad) printf( "Case #%d: IMPOSSIBLE\n", c + 1 );
        else printf( "Case #%d: %d\n", c + 1, res );
    }
    return 0;
}
