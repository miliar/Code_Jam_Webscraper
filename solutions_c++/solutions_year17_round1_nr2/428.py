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
ll mn,mx;
};
ll ar[55],arr[55][55],ary[55][55][5];
bool cmp(T x,T y)
{
    return x.mx<y.mx;
}
vector<T>ele[55];
ll pos[55][55],vis[55];
int main()
{
    ll i,j,k,l,t,cs=1,r=1,s,m,n,a,b,c,d,e,f,g,h,u,v;

  // freopen("B.in","r",stdin);
//freopen("out.txt","w",stdout);
    sn("%lld",&t);
    while(t--)
    {
        sn("%lld %lld",&n,&m);
        for(i=0;i<n;i++)
        {
            sn("%lld",&ar[i]);
        }
        ll mmx=0,mmn=100000000;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                sn("%lld",&arr[i][j]);
                ll lw=0,hi=200000000,mid;
                while(lw<=hi)
                {
                    mid=(lw+hi)/2;
                    u=(mid*ar[i]*90)/100;
                    if((mid*ar[i]*90)%100!=0)
                        u++;
                    v=(mid*ar[i]*110)/100;
                    if(arr[i][j]>=u&&arr[i][j]<=v)
                    {
                        u=((mid-1)*ar[i]*90)/100;
                        if(((mid-1)*ar[i]*90)%100!=0)
                            u++;
                        v=((mid-1)*ar[i]*110)/100;
                        if(mid-1>=0&&arr[i][j]>=u&&arr[i][j]<=v)
                        {
                            hi=mid-1;
                        }
                        else
                        break;
                    }
                    else if(arr[i][j]<u)
                    {
                        hi=mid-1;
                    }
                    else
                    {
                        lw=mid+1;
                    }
                }
                if(lw<=hi&&mid>0)
                {
                    ary[i][j][0]=mid;
                }
                else
                {
                    ary[i][j][0]=-1;
                }
                lw=0,hi=200000000;
                k=hi;
                while(lw<=hi)
                {
                    mid=(lw+hi)/2;
                    u=(mid*ar[i]*90)/100;
                    if((mid*ar[i]*90)%100!=0)
                        u++;
                    v=(mid*ar[i]*110)/100;
                    if(arr[i][j]>=u&&arr[i][j]<=v)
                    {
                        u=((mid+1)*ar[i]*90)/100;
                        if(((mid+1)*ar[i]*90)%100!=0)
                            u++;
                        v=((mid+1)*ar[i]*110)/100;
                        if(arr[i][j]>=u&&arr[i][j]<=v)
                        {
                            lw=mid+1;
                        }
                        else
                        break;
                    }
                    else if(arr[i][j]>v)
                    {
                        lw=mid+1;
                    }
                    else
                    {
                        hi=mid-1;
                    }
                }
                if(lw<=hi&&mid>0)
                {
                    ary[i][j][1]=mid;
                }
                else
                {
                    ary[i][j][1]=-1;
                }
                if(ary[i][j][0]>=0&&ary[i][j][1]>=0)
                {
                    T tmp;
                    tmp.mn=ary[i][j][0];
                    tmp.mx=ary[i][j][1];
                    mmx=max(mmx,tmp.mx);
                    mmn=min(mmn,tmp.mn);
                    ele[i].pb(tmp);
                }
            }
            sort(ele[i].begin(),ele[i].end(),cmp);
        }
        memset(pos,0,sizeof(pos));
        ll ans=0;
        for(i=mmn;i<=mmx;i++)
        {
            c=0;
            for(j=0;j<n;j++)
            {
                d=-1;
               for(k=0;k<ele[j].size();k++)
               {
                   if(pos[j][k]==0&&ele[j][k].mn<=i&&ele[j][k].mx>=i)
                   {
                       d=k;
                       break;
                   }
               }
               if(d==-1)
                break;
                vis[j]=d;
            }
            if(j==n)
            {
                ans++;
                for(j=0;j<n;j++)
                    pos[j][vis[j]]=1;
                i--;
            }
        }
        pf("Case #%lld: %lld\n",cs++,ans);
        for(i=0;i<=n;i++)
        {
            ele[i].clear();
        }
    }
    return 0;

}

/*
#include <bits/stdc++.h>
  #define _ ios_base::sync_with_stdio(0);cin.tie(0);
*/
