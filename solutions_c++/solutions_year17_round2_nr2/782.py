// Artur Kraska, II UWr

#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cmath>
#include <list>
#include <set>
#include <map>

#define forr(i, n)                  for(int i=0; i<n; i++)
#define FOREACH(iter, coll)         for(typeof(coll.begin()) iter = coll.begin(); iter != coll.end(); ++iter)
#define FOREACHR(iter, coll)        for(typeof(coll.rbegin()) iter = coll.rbegin(); iter != coll.rend(); ++iter)
#define lbound(P,R,PRED)            ({typeof(P) X=P,RRR=(R), PPP = P; while(PPP<RRR) {X = (PPP+(RRR-PPP)/2); if(PRED) RRR = X; else PPP = X+1;} PPP;})
#define testy()                     int _tests; scanf("%d", &_tests); FOR(_test, 1, _tests)
#define CLEAR(tab)                  memset(tab, 0, sizeof(tab))
#define CONTAIN(el, coll)           (coll.find(el) != coll.end())
#define FOR(i, a, b)                for(int i=a; i<=b; i++)
#define FORD(i, a, b)               for(int i=a; i>=b; i--)
#define MP                          make_pair
#define PB                          push_back
#define deb(X)                      X;

#define M 1000000007
#define INF 1000000007

using namespace std;

int n, r, b, y, notr, notb, noty;

bool da_sie()
{
    if(r > 0 && notr >= r)
        return 0;
    r -= notr;
    n -= 2*notr;

    if(b > 0 && notb >= b)
        return 0;
    b -= notb;
    n -= 2*notb;

    if(y > 0 && noty >= y)
        return 0;
    y -= noty;
    n -= 2*noty;

//    cout << r << "  " << y << " " << n << endl;
    if(r > n/2 || b > n/2 || y > n/2)
        return 0;

    return 1;
}

void wypisz_r()
{
    printf("R");
    while(notr > 0)
    {
        printf("GR");
        notr--;
    }
    r--;
}

void wypisz_b()
{
    printf("B");
    while(notb > 0)
    {
        printf("OB");
        notb--;
    }
    b--;
}

void wypisz_y()
{
    printf("Y");
    while(noty > 0)
    {
        printf("VY");
        noty--;
    }
    y--;
}

int main()
{
    testy()
    {
        scanf("%d %d %d %d %d %d %d", &n, &r, &notb, &y, &notr, &b, &noty);
        printf("Case #%d: ", _test);

        if(notr == r && 2*r == n)
        {
            forr(i, n/2)
                printf("RG");
            printf("\n");
            continue;
        }
        if(notb == b && 2*b == n)
        {
            forr(i, n/2)
                printf("BO");
            printf("\n");
            continue;
        }
        if(noty == y && 2*y == n)
        {
            forr(i, n/2)
                printf("YV");
            printf("\n");
            continue;
        }

        if(!da_sie())
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            char prio = 'r';
            if(y > r && y > b)
                prio = 'y';
            if(b > r && b > y)
                prio = 'b';

            char last = 0, now = 0;
            int maks = 0;
            while(r + y + b != 0)
            {
                maks = 0;
                if('r' != last && (r > maks || (r == maks && prio == 'r')))
                {
                    maks = r;
                    now = 'r';
                }
                if('b' != last && (b > maks || (b == maks && prio == 'b')))
                {
                    maks = b;
                    now = 'b';
                }
                if('y' != last && (y > maks || (y == maks && prio == 'y')))
                {
                    maks = y;
                    now = 'y';
                }

                if(now == 'r')
                    wypisz_r();
                if(now == 'y')
                    wypisz_y();
                if(now == 'b')
                    wypisz_b();

                last = now;
            }
            printf("\n");
        }
    }

    return 0;
}
