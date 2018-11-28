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
char st[44][44];
int main()
{
    int i,j,k,l,t,cs=1,r=1,s,m,n,a,b,c,d,e,f,g,h,u,v;

   // freopen("A.in","r",stdin);
   // freopen("out.txt","w",stdout);
    sn("%d",&t);
    while(t--)
    {
        sn("%d %d",&n,&m);
        for(i=0;i<n;i++)
        {
            sn("%s",&st[i]);
        }
        for(i='A';i<='Z';i++)
        {
            for(j=0;j<n;j++)
            {
                for(k=0;k<m;k++)
                {
                    if(st[j][k]==i)
                    {
                        u=j;
                        v=k;
                        while(v-1>=0&&st[u][v-1]=='?')
                        {
                            v--;
                            st[u][v]=i;
                        }
                        u=j;
                        v=k;
                        while(v+1<m&&st[u][v+1]=='?')
                        {
                            v++;
                            st[u][v]=i;
                        }
                        j=n+1;
                        break;
                    }
                }
            }
        }
       for(i='A';i<='Z';i++)
        {
            vector<int>X,Y;
            for(j=0;j<n;j++)
            {
                for(k=0;k<m;k++)
                {
                    if(st[j][k]==i)
                    {
                        X.pb(j);
                        Y.pb(k);
                    }
                }
            }
            a=1000,b=1000,c=1000,d=1000;
            for(j=0;j<X.size();j++)
            {
                int cnt=0;
                u=X[j];
                v=Y[j];
                while(u-1>=0&&st[u-1][v]=='?')
                {
                    u--;
                    cnt++;
                }
                a=min(a,cnt);
                u=X[j];
                v=Y[j];
                cnt=0;
                while(u+1<n&&st[u+1][v]=='?')
                {
                    u++;
                    cnt++;
                }
                b=min(b,cnt);
                u=X[j];
                v=Y[j];
                cnt=0;
                while(v-1<n&&st[u][v-1]=='?')
                {
                    v--;
                    cnt++;
                }
                c=min(c,cnt);
                u=X[j];
                v=Y[j];
                cnt=0;
                while(v+1<m&&st[u][v+1]=='?')
                {
                    v++;
                    cnt++;
                }
                d=min(d,cnt);
            }
            for(j=0;j<X.size();j++)
            {
                int cnt=0;
                u=X[j];
                v=Y[j];
                cnt =a;
                while(cnt--)
                {
                    u--;
                    st[u][v]=i;
                }
                u=X[j];
                v=Y[j];
                cnt=b;
                while(cnt--)
                {
                    u++;
                    st[u][v]=i;
                }
                u=X[j];
                v=Y[j];
                cnt=c;
                while(cnt--)
                {
                    v--;
                    st[u][v]=i;
                }
                u=X[j];
                v=Y[j];
                cnt=d;
                while(cnt--)
                {
                    v++;
                    st[u][v]=i;
                }
            }
        }
        pf("Case #%d:\n",cs++);
        for(i=0;i<n;i++)
            pf("%s\n",st[i]);
    }
    return 0;

}

/*
#include <bits/stdc++.h>
  #define _ ios_base::sync_with_stdio(0);cin.tie(0);
*/
