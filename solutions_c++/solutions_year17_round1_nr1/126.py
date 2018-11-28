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

const int MR = 30;

char s[MR][MR];

int main()
{
    int T;
    scanf( "%d", &T );
    REP( c, T )
    {
        int R, C;
        scanf( "%d%d", &R, &C );
        REP( i, R )
            scanf( "%s", s[i] );
        REP( i, R )
        {
            REP( j, C )
            {
                if (s[i][j] != '?')
                {
                    int k = j - 1;
                    while (k >= 0 && s[i][k] == '?')
                    {
                        s[i][k] = s[i][j];
                        k--;
                    }
                    k = j + 1;
                    while (k < C && s[i][k] == '?')
                    {
                        s[i][k] = s[i][j];
                        k++;
                    }
                }
            }
        }

        REP( i, C )
        {
            REP( j, R )
            {
                if (s[j][i] != '?')
                {
                    int k = j - 1;
                    while (k >= 0 && s[k][i] == '?')
                    {
                        s[k][i] = s[j][i];
                        k--;
                    }
                    k = j + 1;
                    while (k < R && s[k][i] == '?')
                    {
                        s[k][i] = s[j][i];
                        k++;
                    }
                }
            }
        }

        printf( "Case #%d:\n", c + 1 );

        REP( i, R )
            printf( "%s\n", s[i] );
        
    }
    return 0;
}
