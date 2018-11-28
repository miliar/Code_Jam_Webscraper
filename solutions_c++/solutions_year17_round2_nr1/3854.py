#include <stdio.h>
#include <algorithm>
#define maxn 1005
using namespace std;

int T,N,D;
double x[maxn], v[maxn], xx[maxn],vv[maxn];
double d[maxn], a[maxn], b[maxn];

int ind[maxn];


bool cmp(int i,int j)
{
    return x[i]<x[j];
}

void read()
{
    scanf("%d %d",&D,&N);
    for(int i=1;i<=N;i++)
        scanf("%lf %lf",&x[i],&v[i]);

    x[N+1] = D; v[N+1] = 0;
}

void solve()
{
    for(int i=1;i<=N;i++) ind[i]=i,xx[i]=x[i],vv[i]=v[i];
    sort(ind+1, ind+N+1, cmp);

    for(int i=1;i<=N;i++)
    {
        x[i] = xx[ind[i]];
        v[i] = vv[ind[i]];

    }

    double sol;

    while(N)
    {
         double Min = -1;
         int pos = 0;

         for(int i=1;i<=N;i++)
         {
             d[i] = (x[i+1]-x[i])/(v[i]-v[i+1]);

            if( d[i]>=0 && (d[i] < Min || Min == -1 ) )
            {
                Min = d[i];
                pos = i;
            }
         }


        for(int i=1;i<pos;i++) x[i] += v[i]*Min;

        for(int i=pos;i<=N;i++)
        {
            x[i] = x[i+1];
            v[i] = v[i+1];
            x[i] += v[i]*Min;
        }

        sol+=Min;
        N--;
    }
    double cnt = 1.0*D/sol;
    printf("%f\n",cnt);
}

int main()
{
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);

    scanf("%d",&T);
    for(int it=1;it<=T;it++)
    {
        printf("Case #%d: ",it);
        read();
        solve();
    }

    return 0;
}
