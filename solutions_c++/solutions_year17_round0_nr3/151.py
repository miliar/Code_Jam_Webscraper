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
vector<ll>ar;
set<ll>vis;
map<ll,ll>dp;
void rec(ll n)
{
    if(n==0)
        return;
    if(vis.count(n))
        return;
    vis.insert(n);
    ar.pb(n);
    if(n%2==0)
    {
        rec(n/2);
        rec((n/2)-1);
    }
    else
        rec(n/2);
}
int main()
{
    ll i,j,k,l,t,cs=1,r=1,s,m,n,a,b,c,d,e,f,g,h,u,v;

    //freopen("C.in","r",stdin);
    //freopen("out.txt","w",stdout);
    //freopen("out.txt","w",stdout);
   sn("%lld",&t);
   while(t--)
   {
       sn("%lld %lld",&n,&k);
       rec(n);
       sort(ar.begin(),ar.end());
       for(i=ar.size()-1;i>=0;i--)
       {
           dp[ar[i]]=0;
           if(ar.size()==i+1)
           dp[ar[i]]=1;
       }
       ll ans=0;
       for(i=ar.size()-1;i>=0;i--)
       {
           u=dp[ar[i]];
           if(k<=u)
           {
               ans=ar[i];
               break;
           }
           else
           {
               k=k-u;
           }
           if(ar[i]%2==0)
           {
               a=ar[i]/2;
               b=a-1;
               dp[a]=dp[a]+u;
               dp[b]=dp[b]+u;
           }
           else
           {
               a=ar[i]/2;
               b=a-1;
               dp[a]=dp[a]+u+u;
           }
       }
       a=ans/2;
       b=a;
       if(ans%2==0)
        b=a-1;
       pf("Case #%lld: %lld %lld\n",cs++,a,b);
       vis.clear();
       dp.clear();
       ar.clear();
   }
    return 0;

}

/*
#include <bits/stdc++.h>
  #define _ ios_base::sync_with_stdio(0);cin.tie(0);
*/
