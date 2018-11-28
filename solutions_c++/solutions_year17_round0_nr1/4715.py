#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define pii pair<long long,long long>
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define PI 3.14159265
#define ll long long
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define debug(x) cout << #x << " = " << x << endl
#define INF 1000000009
#define mod 1000000007

int main()
{
     ios::sync_with_stdio(0);
     ll int n,k;
     cin>>n;
     string s;
     ll int flag;
     ll int caser=0;
     ll int count;
     for(int i=0;i<n;i++)
     {
         count=0;
         flag=0;
         caser++;
         cin>>s;
         cin>>k;
         for(int i=0;i<s.size();i++)
         {
             
             if(s[i]=='-')
             {
                 count++;
                 if(i+k-1<=s.size()-1)
                 {
                     for(int j=i;j<=i+k-1;j++)
                     {
                         if(s[j]=='+')
                         s[j]='-';
                         else
                         s[j] = '+';
                     }
                 }
                 else
                 {
                     flag=1;
                 }
             }
             
         }
         if(flag==1)
         {
             cout<<"Case #"<<caser<<": "<<"IMPOSSIBLE"<<"\n";
         }
         else
          cout<<"Case #"<<caser<<": "<<count<<"\n";
         
         
         
         
     }

    return 0;
}