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

int main()
{
    int T;
    scanf( "%d", &T );
    REP( c, T )
    {
        LL N, K;
        scanf( "%lld%lld", &N, &K );

        LL mn, mx, ile = 0;
        map<LL, LL> M;
        M[N] = 1;
        
        while (ile < K)
        {
            auto it = M.end(); it--;
            auto v = *it;
            M.erase( it );

            LL m1 = v.first / 2;
            LL m2 = v.first / 2;
            if (v.first % 2 == 0)
                m1--;
            if (ile + v.second >= K)
            {
                mx = m2;
                mn = m1;
                break;
            }

            ile += v.second;
            M[m1] += v.second;
            M[m2] += v.second;
        }

        printf( "Case #%d: %lld %lld\n", c + 1, mx, mn );
    }
    return 0;
}
