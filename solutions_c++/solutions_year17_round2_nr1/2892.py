#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <cmath>
#include <list>
#include <bitset>
using namespace std;

#define pi pair<int,int>
#define mp(x,y) make_pair(x,y)
#define fi first
#define se second
#define pl pair<long long,long long>
#define pb push_back
#define vi vector<int>
#define ll long long
#define ALL(c) c.begin(),c.end()
#define VAR(v,n) __typeof(n) v=(n)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)

const int MAXN=1005;

struct hor
{
    double start,speed;

    friend bool operator < (hor a, hor b)
    {
        return a.start<b.start;
    }
};

hor t[1005];
list<hor> l;

int main ()
{
    int a,b,c,d,e,f,g,num,n;
    double x,y,z,pos;
    list<hor>::iterator it,it2;

    scanf ("%d", &num);

    for (f=1; f<=num; f++)
    {
        scanf("%d%d", &d, &n);

        for (a=0; a<n; a++)
            scanf("%lf%lf", &t[a].start, &t[a].speed);

        sort(t,t+n);
        l.clear();

        for (a=0; a<n; a++)
            l.pb(t[a]);

        z=0;

        while (1)
        {
            x=-1;

            for (it=l.begin(); 1; it++)
            {
                it2=it;
                it2++;

                if (it2==l.end())
                    break;

                if (it->speed>it2->speed)
                {
                    y=(it2->start-it->start)/(it->speed-it2->speed);

                    if (it2->start+y*it2->speed<d)
                    {
                        if (x==-1)
                            x=y;
                        else if (x>y)
                            x=y;
                    }
                }
            }

            if (x==-1)
                break;

            z+=x;

            for (it=l.begin(); it!=l.end(); it++)
            {
                it->start+=x*it->speed;

                if (it!=l.begin())
                {
                    it2=it;
                    it2--;

                    if (it2->start==it->start)
                        l.erase(it2);
                }
            }
        }

        it=l.begin();
        printf("Case #%d: %lf\n", f, (double)d/(z+((double)d-it->start)/it->speed));
    }

    return 0;
}
