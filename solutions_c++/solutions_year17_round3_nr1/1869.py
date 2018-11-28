#include <iostream>
#include<fstream>
#include<algorithm>
#include<iomanip>
using namespace std;
#define pi 3.14159265359
ifstream f("input");
ofstream g("output");
int t,it,n,k,i,j;
int sel[1001];
long double sol,curr,mx;
struct clatita
{
    long double h,r;
    int p;
}v[1001],w[1001];
inline bool cmp(clatita a,clatita b)
{
    return(a.r*a.h>b.r*b.h);
}
inline bool cmp1(clatita a,clatita b)
{
    long double x,y;
    x=a.r*(a.r+2*a.h);
    y=b.r*(b.r+2*b.h);
    return ( x > y );
}
inline bool cmp2(clatita a, clatita b)
{
    if(sel[a.p]==sel[b.p])
    {
        return(a.r>b.r);
    }
    else
        return(sel[a.p]>sel[b.p]);
}
int main()
{
    f>>t;
    for(it=1;it<=t;++it)
    {
        for(i=1;i<=n;++i)sel[i]=0;
        f>>n>>k;curr=0;sol=0;
        for(i=1;i<=n;++i)
            f>>w[i].r>>w[i].h;
        for(i=1;i<=n;++i)
        {
            for(j=1;j<=n;++j)v[j]=w[j];
            curr=v[i].r*v[i].r+2*v[i].h*v[i].r;
            swap(v[i],v[1]);
            sort(v+2,v+1+n,cmp);
            for(j=2;j<=k;++j)
                curr+=2*v[j].r*v[j].h;
            sol=max(sol,curr);
        }
        sol=sol*pi;
        g<<"Case #"<<it<<": ";
        g<<fixed<<setprecision(6)<<sol;
        g<<'\n';
    }
    return 0;
}
