#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;
#define ll long long
vector<int>v;
ll pw(ll a,ll b)
{
  ll x=1;
  while(b)
  {
    if(b&1)
     x*=a;
    a*=a;
    b>>=1;
  }
  return x;
};
int main()
{
  //freopen("B-large.in", "r", stdin);
  //freopen("a.out", "w", stdout);
  int t,i,j;
  ll n,ans,cnt;
  scanf("%d",&t);
  for(i=1;i<=t;i++)
  {
     ans=0;
     cin>>n;
     ll cur=n;
     v.clear();
     while(cur)
     {
       v.push_back(cur%10);
       cur/=10;
     }
     reverse(v.begin(),v.end());
     cnt=0;
     int k;
     for(j=0;j<v.size()-1;j++)
     {
       if(v[j]<=v[j+1])
        continue;
       k=j;
       while(k>0)
       {
         if(v[k]==v[k-1])
          k--;
         else
           break;
       }
       //cout<<k<<endl;
       if(k==-1)
        k++;
       v[k]=v[k]-1;
       for(k=k+1;k<v.size();k++)
        v[k]=9;
         break;
     }
     for(j=0;j<v.size();j++)
      cnt+=(ll)v[j]*(pw(10,v.size()-j-1));
     cout<<"Case #"<<i<<": "<<cnt<<endl;
  }
  return 0;
}
