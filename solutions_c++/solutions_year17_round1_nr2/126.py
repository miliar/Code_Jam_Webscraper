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

const int MR = 60;

int Q[MR][MR], R[MR];

int main()
{
    int T;
    scanf( "%d", &T );
    REP( c, T )
    {
        int res = 0;
        int N, P;
        scanf( "%d%d", &N, &P );
        REP( i, N )
        {
            scanf( "%d", &R[i] );
            R[i] *= 10;
        }
        REP( i, N )
        {
            REP( j, P )
            {
                scanf( "%d", &Q[i][j] );
                Q[i][j] *= 10;
            }
            sort( Q[i], Q[i] + P );
        }

        int mn = 1;
        while (true)
        {
            bool ok = 1;
            REP( i, N )
            {
                // zobacz czy mozna ulozyc
                if (Q[i][P - 1] < mn*R[i] / 10 * 9)
                {
                    ok = 0;
                    break;
                }
            }

            if (!ok)
                break;

            // probuj ulozyc
            vector < int > pom( N, -1 );

            REP( i, N )REP( j, P )
            {
                if (Q[i][j] >= mn*R[i] / 10 * 9 && Q[i][j] <= mn*R[i] / 10 * 11)
                {
                    pom[i] = j;
                    break;
                }
            }

            REP( i, N )
            {
                if (pom[i] == -1)
                {
                    ok = 0;
                    break;
                }
            }

            // jesli sie nie udalo, sprobuj cos wiekszego
            if (!ok)
            {
                mn++;
                continue;
            }

            res++;
            REP( i, N )
            {
                Q[i][pom[i]] = 0;
                sort( Q[i], Q[i] + P );
            }
        }

        printf( "Case #%d: %d\n", c + 1, res );
    }
    return 0;
}
