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

int n, m, ile;
char slowo[1007][1007];
int numer[1007][1007];

struct laser
{
    int w, k;
    int pion;
    int poziom;
};
laser tab[1000007];

vector <pair<int, int> > v;

bool dzialaj(int nr)
{
    if(nr == ile)
    {
        FOREACH(it, v)
        {
            if(!(tab[it->first].pion || tab[it->second].poziom))
                return 0;
        }
        return 1;
    }
    if(tab[nr].pion == 0 || tab[nr].poziom == 0)
    {
        if(dzialaj(nr+1))
            return 1;
    }
    else
    {
        tab[nr].pion = 0;
        slowo[tab[nr].w][tab[nr].k] = '-';
        if(dzialaj(nr+1))
            return 1;
        tab[nr].pion = 1;
        tab[nr].poziom = 0;
        slowo[tab[nr].w][tab[nr].k] = '|';
        if(dzialaj(nr+1))
            return 1;
        tab[nr].poziom = 1;
    }
    return 0;
}

bool dzialaj()
{
    v.clear();

    forr(nr, ile)
    {
        int w = tab[nr].w;
        int k = tab[nr].k;
        FOR(i, w+1, n-1)
        {
            if(slowo[i][k] == '#')
                break;
            if(slowo[i][k] == '|' || slowo[i][k] == '-')
            {
                tab[nr].pion = 0;
                break;
            }
        }
        FORD(i, w-1, 0)
        {
            if(slowo[i][k] == '#')
                break;
            if(slowo[i][k] == '|' || slowo[i][k] == '-')
            {
                tab[nr].pion = 0;
                break;
            }
        }

        FOR(j, k+1, m-1)
        {
            if(slowo[w][j] == '#')
                break;
            if(slowo[w][j] == '|' || slowo[w][j] == '-')
            {
                tab[nr].poziom = 0;
                break;
            }
        }
        FORD(j, k-1, 0)
        {
            if(slowo[w][j] == '#')
                break;
            if(slowo[w][j] == '|' || slowo[w][j] == '-')
            {
                tab[nr].poziom = 0;
                break;
            }
        }
        if(tab[nr].pion == 0)
        {
            slowo[w][k] = '-';
        }
        else
            slowo[w][k] = '|';
        if(!(tab[nr].pion || tab[nr].poziom))
            return 0;
    }


    forr(i, n)
        forr(j, m)
            if(slowo[i][j] == '.')
            {
                int pion = -1, poziom = -1;
                FOR(i1, i+1, n-1)
                {
                    if(slowo[i1][j] == '#')
                        break;
                    if(slowo[i1][j] == '|' || slowo[i1][j] == '-')
                    {
                        pion = numer[i1][j];
                        break;
                    }
                }
                FORD(i1, i-1, 0)
                {
                    if(slowo[i1][j] == '#')
                        break;
                    if(slowo[i1][j] == '|' || slowo[i1][j] == '-')
                    {
                        pion = numer[i1][j];
                        break;
                    }
                }

                FOR(j1, j+1, m-1)
                {
                    if(slowo[i][j1] == '#')
                        break;
                    if(slowo[i][j1] == '|' || slowo[i][j1] == '-')
                    {
                        poziom = numer[i][j1];
                        break;
                    }
                }
                FORD(j1, j-1, 0)
                {
                    if(slowo[i][j1] == '#')
                        break;
                    if(slowo[i][j1] == '|' || slowo[i][j1] == '-')
                    {
                        poziom = numer[i][j1];
                        break;
                    }
                }

                if(!tab[poziom].poziom)
                    poziom = -1;
                if(!tab[pion].pion)
                    pion = -1;

                if(pion == -1 && poziom == -1)
                    return 0;
                if(pion == -1)
                {
                    tab[poziom].pion = 0;
                    slowo[tab[poziom].w][tab[poziom].k] = '-';
                }
                if(poziom == -1)
                {
                    tab[pion].poziom = 0;
                    slowo[tab[pion].w][tab[pion].k] = '|';
                }
                if(pion >= 0 && poziom >= 0)
                {
                    v.PB(MP(pion, poziom));
                }
            }

    FOREACH(it, v)
    {
        if(!(tab[it->first].pion || tab[it->second].poziom))
            return 0;
    }

    if(dzialaj(0))
        return 1;

    return 0;
}

int main()
{
    testy()
    {
        scanf("%d %d", &n, &m);
        ile = 0;
        forr(i, n)
        {
            scanf("%s", slowo[i]);
            forr(j, m)
            {
                if(slowo[i][j] == '|' || slowo[i][j] == '-')
                {
                    tab[ile].w = i;
                    tab[ile].k = j;
                    tab[ile].pion = 1;
                    tab[ile].poziom = 1;
                    numer[i][j] = ile;
                    ile++;
                }
            }
        }
        if(dzialaj())
        {
            printf("Case #%d: POSSIBLE\n", _test);
            forr(i, n)
            {
                printf("%s\n", slowo[i]);
            }
        }
        else
            printf("Case #%d: IMPOSSIBLE\n", _test);
    }

    return 0;
}
