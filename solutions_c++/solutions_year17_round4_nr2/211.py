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

int res, n, m, c, krzeslo[1000007], maks_klient, klient[1000007];

bool dzialaj(int ile)
{
    res = 0;
    int zostalo = 0;

    FOR(i, 1, n)
    {
        int x = min(ile, krzeslo[i]);
        zostalo += ile;
        if(krzeslo[i] > zostalo)
            return false;

        res += krzeslo[i] - x;
        zostalo -= krzeslo[i];
    }

    return true;
}

int main()
{
    testy()
    {
        scanf("%d %d %d", &n, &c, &m);
        CLEAR(klient);
        CLEAR(krzeslo);
        maks_klient = 0;
        forr(i, m)
        {
            int a, b;
            scanf("%d %d", &a, &b);
            klient[b]++;
            maks_klient = max(maks_klient, klient[b]);
            krzeslo[a]++;
        }

        int pocz = maks_klient, kon = m, s;
        while(pocz < kon)
        {
            s = (pocz + kon)/2;
            if(dzialaj(s))
            {
                kon = s;
            }
            else
                pocz = s+1;
        }
        dzialaj(pocz);
        printf("Case #%d: %d %d\n", _test, pocz, res);
    }

    return 0;
}
