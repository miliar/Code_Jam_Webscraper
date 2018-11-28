#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back





int main() {
    freopen("jammm.in", "r", stdin);
  freopen("jammm.out", "w", stdout);
    ll tt;
    cin>>tt;
     for (ll qq=1;qq<=tt;qq++)
 {

     ll numb;
     cin>>numb;
     vector<ll> v;

    while(numb>0)
    {
       ll k=numb%10;
       v.pb(k);
       numb=numb/10;

    }
    reverse(v.begin(),v.end());


 /*for(ll i=0;i<v.size();i++)
     {
         cout<<v[i];
     }
     //cout<<v.size();*/
     for(ll i=0;i<v.size()-1;i++)
     {
         if(v[i]>v[i+1])
         {
            v[i]=v[i]-1;
         for(ll j=i+1;j<v.size();j++)
         {
             v[j]=9;
         }
         i=i-2;
          if(i<0)
            i=-1;

         }

     }
cout<<"Case #"<<qq<<":"<<" ";
if(v[0]==0)
{
 for(ll i=1;i<v.size();i++)
 {
     cout<<v[i];
 }
}
 else
 {
 for(ll i=0;i<v.size();i++)
 {
     cout<<v[i];
 }
 }
cout<<"\n";
 }
  return 0;
}
