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

long long n;
int tab[1000];

int main()
{
    testy()
    {
        scanf("%lld", &n);
        int dl = 0;
        tab[dl++] = 10;
        while(n > 0)
        {
            tab[dl++] = n%10;
            n /= 10;
        }
        int incr = dl-1;
        FORD(i, dl-2, 0)
        {
            if(tab[i+1] < tab[i])
                incr = i;
            if(tab[i] < tab[i+1])
            {
                break;
            }
        }
        FOR(i, 0, incr-1)
        {
            tab[i] = 9;
        }
        tab[incr]--;
        while(tab[dl-1] == 0)
            dl--;
        printf("Case #%d: ", _test);
        FORD(i, dl-1, 1)
            printf("%d", tab[i]);
        printf("\n");
    }


    return 0;
}
