#include <iostream>
#include<iomanip>
#include<fstream>
#include<vector>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
#define DIM 100000
#define M 666013
int poz;
char buff[DIM];
ifstream f("input");
ofstream g("output");
inline void R(int &x)
{
    x=0;
    char semn='+';
    while(buff[poz]<'0' || buff[poz]>'9')
    {
        semn=buff[poz];
        if(++poz==DIM)
        {
            poz=0;
            f.read(buff,DIM);
        }
    }
    while(buff[poz]>='0' && buff[poz]<='9')
    {
        x=x*10+buff[poz]-'0';
        if(++poz==DIM)
        {
            poz=0;
            f.read(buff,DIM);
        }
    }
    if(semn=='-')x=-x;
}
vector<int>h[M];
inline void ad(int val)
{
    int x,m=val%M;
    for(int i=0;i<h[m].size();++i)
    {
        x=h[m][i];
        if(x==val)return;
    }
    h[m].push_back(val);
}

inline bool S(int val)
{
    int x,m=val%M;
    for(int i=0;i<h[m].size();++i)
    {
        x=h[m][i];
        if(x==val)return 1;
    }
    return 0;
}
int t,it,n,i,j;
long double curr,d,p,s,sol,mx;

int main()
{
    f>>t;
    for(it=1;it<=t;++it)
    {
        f>>d>>n;
        sol=0;mx=0;
        for(i=0;i<n;++i)
        {
            f>>p>>s;
            curr=(d-p)/s;
            mx=max(curr,mx);
        }
        sol=d/mx;
        g<<"Case #"<<it<<": "<<fixed<<setprecision(15)<<sol<<'\n';
    }
    return 0;
}
