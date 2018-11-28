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

const int inf = 1e9;

set<tuple<int, int, int, int>> S;
queue < pair<tuple<int, int, int, int>, int>> Q;

int gHd, gAd, gHk, gAk, B, D;

int go( tuple<int, int, int, int> initial)
{
    Q.push( MP( initial, 0 ) );
    S.insert( initial );

    while (!Q.empty())
    {
        auto process = Q.front(); Q.pop();
        auto state = process.first;
        int cur = process.second;

        int Hd = get<0>( state );
        int Ad = get<1>( state );
        int Hk = get<2>( state );
        int Ak = get<3>( state );

        // czy mozesz zakonczyc to w tej rundzie
        if (Ad >= Hk)
            return cur + 1;

        // wykonaj kazdy ruch po kolei
        if (Hd > Ak)// spr czy przetrwasz atakujac
        {
            auto s = state;
            get<0>( s ) = Hd - Ak;
            get<2>( s ) = Hk - Ad;
            if (S.find( s ) == S.end())
            {
                S.insert( s );
                Q.push( MP( s, cur + 1 ) );
            }

            // sprobuj zwiekszyc swoja moc
            s = state;
            get<0>( s ) = Hd - Ak;
            get<1>( s ) = Ad + B;
            if (S.find( s ) == S.end())
            {
                S.insert( s );
                Q.push( MP( s, cur + 1 ) );
            }
        }

        if (Hd > Ak - D)
        {
            auto s = state;
            get<0>( s ) = Hd - max( Ak - D, 0 );
            get<3>( s ) = max( 0, Ak - D );
            if (S.find( s ) == S.end())
            {
                S.insert( s );
                Q.push( MP( s, cur + 1 ) );
            }
        }

        if (gHd > Ak)
        {
            auto s = state;
            get<0>( s ) = gHd - Ak;
            if (S.find( s ) == S.end())
            {
                S.insert( s );
                Q.push( MP( s, cur + 1 ) );
            }
        }
    }

    return inf;
}

int main()
{
    int T;
    scanf( "%d", &T );
    REP( c, T )
    {
        scanf( "%d%d%d%d%d%d", &gHd, &gAd, &gHk, &gAk, &B, &D );
        
        int res = go( tuple<int, int, int, int>( gHd, gAd, gHk, gAk ) );
        printf( "Case #%d: ", c + 1 );
        if (res == inf)
            printf( "IMPOSSIBLE\n" );
        else
            printf( "%d\n", res );

        S.clear();
        while (!Q.empty())
            Q.pop();
    }
    return 0;
}
