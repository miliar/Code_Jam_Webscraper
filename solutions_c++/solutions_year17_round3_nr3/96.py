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
double t[55];

int main ()
{
    int a,b,c,d,e,f,g,num,n;
    double u,w,x,y;
    scanf ("%d", &num);

    for (f=1; f<=num; f++)
    {
        scanf("%d%d%lf", &n, &n, &u);

        for (a=0; a<n; a++)
            scanf("%lf", &t[a]);

        t[n++]=1.0;
        sort(t,t+n);

        for (a=0; a+1<n && u>0; a++)
        {
            x=t[a+1]-t[a];

            if (x*(a+1)<u)
            {
                u-=x*(a+1);

                for (b=0; b<=a; b++)
                    t[b]=t[a+1];
            }
            else
            {
                x=u/(double)(a+1);

                for (b=0; b<=a; b++)
                    t[b]+=x;

                u=0;
            }
        }

        w=1;

        for (a=0; a<n; a++)
            w*=t[a];

        printf("Case #%d: %.14lf\n", f, w);

    }

    return 0;
}
