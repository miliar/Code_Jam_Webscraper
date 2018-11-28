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
        LL N;
        scanf( "%lld", &N );
        
        LL mn = 1;
        LL prev = 9;
        LL res = N;

        while (N)
        {
            if (N % 10 > prev)
            {
                // obniz o 1 pozycje i z tylu same 9 daj
                N--;
                res = N*mn + mn - 1;
                prev = N % 10;
            }
            else
                prev = N % 10;

            mn *= 10;
            N /= 10;
        }

        printf( "Case #%d: %lld\n", c + 1, res );
    }
    return 0;
}
