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

int n, m, p, k;
int d[1007][1007];
map <pair<int, int> , double > best;
map <pair<double, pair<int, int> >, double > mapa;

struct konie{
    int dist;
    int speed;
};
konie tab[1007];

double dzialaj(int pocz, int kon)
{
    best.clear();
    mapa.clear();

    mapa[MP(0, MP(pocz, pocz))] = 0;

    while(!mapa.empty())
    {
        double time = mapa.begin()->first.first;
        int city = mapa.begin()->first.second.first;
        int horse = mapa.begin()->first.second.second;
        int left = mapa.begin()->second;

//        cout << " jest w " << city << " z koniem " << horse << " i czasem " << time << endl;

        mapa.erase(mapa.begin());

        if(city == kon)
        {
            return time;
        }

        FOR(i, 1, n)
        {
            double time2 = time+(d[city][i]/(double)tab[horse].speed);
            if(d[city][i] != -1 && d[city][i] <= left && (!CONTAIN(MP(i, horse), best) || best[MP(i, horse)] > time2))
            {
                best[MP(i, horse)] = time2;
                mapa[MP(time2, MP(i, horse))] = left - d[city][i];
            }

            time2 = time+(d[city][i]/(double)tab[city].speed);
            if(d[city][i] != -1 && d[city][i] <= tab[city].dist && (!CONTAIN(MP(i, i), best) || best[MP(i, city)] > time2))
            {
                best[MP(i, city)] = time2;
                mapa[MP(time2, MP(i, city))] = tab[city].dist - d[city][i];
            }
        }
    }

    return 0;
}

int main()
{
    testy()
    {
        scanf("%d %d", &n, &m);
        FOR(i, 1, n)
            scanf("%d %d", &tab[i].dist, &tab[i].speed);
        FOR(i, 1, n)
            FOR(j, 1, n)
                scanf("%d", &d[i][j]);

        printf("Case #%d:", _test);
        forr(x, m)
        {
            scanf("%d %d", &p, &k);
            printf(" %.10lf", dzialaj(p, k));
        }
        printf("\n");
    }

    return 0;
}
