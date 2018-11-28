
//BISMILLAHIR RAHMANIR RAHIM
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<queue>
#include<set>
#include <iostream>
#include<stack>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#define N 1000000
#define sn scanf
#define pf printf
#define pb push_back
#define mp make_pair

const double PI=2.0*acos(0);

typedef long long int ll;
using namespace std;
struct T{
int a;
};
struct vec{
double x,y;
 vec(double xx=0,double yy=0)
 {
     x=xx;y=yy;
 }
};
vec make_vac(vec p,vec q)
{
    return vec(q.x-p.x,q.y-p.y);
}
double dotproduct(vec p,vec q)
{
    return p.x*q.x+p.y*q.y;
}
double crossproduct(vec p,vec q)
{
    return p.x*q.y-q.x*p.y;
}
double vec_value(vec p)
{
    return sqrt(p.x*p.x + p.y*p.y);
}
vec unit_vec(vec p)
{
    double va=vec_value(p);
    return vec(p.x/va,p.y/va);
}
double dis(double px,double py,double qx,double qy)
{
    px=fabs(px-qx);
    py=fabs(py-qy);
    return sqrt(px*px+py*py);
}
ll bigmod(ll a,ll b,ll mod)
{
    if(b==0)return 1;
    if(b%2==0)
    {
        ll hh=bigmod(a,b/2,mod);
        return (hh*hh)%mod;
    }
    else
    {
       return (a*bigmod(a,b-1,mod))%mod;
    }
}
int vis[100];
int dp[101][101][101][4][5];

int rec(int on,int tw,int th,int rem,int p)
{
    if(on+tw+th==0)
        return 0;
    int &ret=dp[on][tw][th][rem][p];
    if(ret!=-1)
        return ret;
    ret=0;
    int fl=0,tmp;
    if(rem==0)
        fl=1;
    if(on>0)
    {
        if(rem>=1)
        {
            tmp=rem-1;
        }
        else
        {
            tmp=1-rem;
            tmp=p-tmp;
        }
        ret=max(ret,fl+rec(on-1,tw,th,tmp,p));
    }
    if(tw>0)
    {
        if(rem>=2)
        {
            tmp=rem-2;
        }
        else
        {
            tmp=2-rem;
            tmp=p-tmp;
        }
        ret=max(ret,fl+rec(on,tw-1,th,tmp,p));
    }
    if(th>0)
    {
        if(rem>=3)
        {
            tmp=rem-3;
        }
        else
        {
            tmp=3-rem;
            tmp=p-tmp;
        }
        ret=max(ret,fl+rec(on,tw,th-1,tmp,p));
    }
    return ret;
}

int main()
{
    int i,j,k,l,t,cs=1,r=1,s,m,n,a,b,c,d,e,f,g,h,u,v;

    //freopen(".txt","r",stdin);
    //freopen(".txt","w",stdout);
    sn("%d",&t);
    memset(dp,-1,sizeof(dp));
    while(t--)
    {
        sn("%d %d",&n,&k);
        memset(vis,0,sizeof(vis));
        for(i=0;i<n;i++)
        {
            sn("%d",&u);
            vis[(u%k)]++;
        }
        int ans=0;
        ans=ans+vis[0];

        pf("Case #%d: %d\n",cs++,ans+rec(vis[1],vis[2],vis[3],0,k));
    }
    return 0;

}

/*
#include <bits/stdc++.h>
  #define _ ios_base::sync_with_stdio(0);cin.tie(0);
*/
