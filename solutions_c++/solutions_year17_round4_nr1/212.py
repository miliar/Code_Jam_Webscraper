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

int n, p, a, suma, tab[10007];

int main()
{
    testy()
    {
        scanf("%d %d", &n, &p);
        CLEAR(tab);
        suma = 0;
        forr(i, n)
        {
            scanf("%d", &a);
            tab[a%p]++;
            suma += a;
        }
        int res = 1 - (suma%p == 0);
        res += tab[0];
        if(p == 2)
        {
            res += tab[1]/2;
        }
        else if(p == 3)
        {
            int x = min(tab[1], tab[2]);
            res += x;
            tab[1] -= x;
            tab[2] -= x;
            res += tab[1]/3;
            res += tab[2]/3;
        }
        else
        {
            res += tab[2]/2;
            tab[2] %= 2;
            int x = min(tab[1], tab[3]);
            res += x;
            tab[1] -= x;
            tab[3] -= x;

            tab[2] += tab[1]/2;
            tab[2] += tab[3]/2;
            res += tab[2]/2;
        }
        printf("Case #%d: %d\n", _test, res);
    }

    return 0;
}
