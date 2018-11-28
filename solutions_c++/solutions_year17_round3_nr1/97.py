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
pair<double,double> pan[MAXN];
double pii=3.14159265358979323846;
priority_queue<double> side;

int main ()
{
    int a,b,c,d,e,f,g,num,n,k;
    double x,y,z;
    scanf ("%d", &num);

    for (f=1; f<=num; f++)
    {
        scanf("%d%d", &n, &k);

        for (a=0; a<n; a++)
        {
            scanf("%lf%lf", &x, &y);
            pan[a]=mp(x,y);
        }

        sort(pan,pan+n);
        x=0;

        for (a=n-1; a+1>=k; a--)
        {
            y=pan[a].fi*pan[a].fi*pii;
            y+=pan[a].fi*pii*2.0*pan[a].se;

            for (b=0; b<a; b++)
                side.push(pan[b].fi*pii*2.0*pan[b].se);

            for (b=2; b<=k; b++)
            {
                y+=side.top();
                side.pop();
            }

            while (!side.empty())
                side.pop();

            x=max(x,y);
        }

        printf("Case #%d: %.10lf\n", f, x);
    }

    return 0;
}
