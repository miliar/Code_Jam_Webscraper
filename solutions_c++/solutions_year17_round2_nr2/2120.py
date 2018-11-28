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
vector< pair<ll int ,char> >v;
bool comp( pair< ll int,char >p, pair< ll int,char > q)
{
    return p.first>q.first;
}
vector<char >ans;
int main()
{
     ios::sync_with_stdio(0);
     ll int t;
     cin>>t;
     ll int caser=0;
     ll int N, R, O, Y, G, B, V;
     while(t--)
     {
         for(int i=0;i<3;i++)
          v.clear();
          
         caser++;
         cin>>N>>R>>O>>Y>>G>>B>>V;
         //cout<<N<<R<<O<<Y<<G<<B<<V;
         v.push_back(make_pair(R,'R'));
         v.push_back(make_pair(Y,'Y'));
         v.push_back(make_pair(B,'B'));
         
     
     sort(v.begin(),v.end(),comp);
     while(v[1].first!=v[2].first)
     {
         ans.push_back(v[0].second);
         ans.push_back(v[1].second);
         v[0].first--;
         v[1].first--;
     }
     if(v[1].first*2<v[0].first)
     {
         cout<<"Case #"<<caser<<": "<<"IMPOSSIBLE";
         cout<<"\n";
     }
     else
     {
         cout<<"Case #"<<caser<<": ";
         for(int i=0;i<ans.size();i++)
         cout<<ans[i];
         ll int m = v[0].first;
         for(int i =0;i<v[1].first;i++)
         {
             if(m>0)
             {
                 cout<<v[0].second;
                 m--;
             }
             cout<<v[1].second;
             if(m>0)
             {
                   cout<<v[0].second;
                 m--;
             }
             cout<<v[2].second;
         }
         cout<<"\n";
     }
   
     ans.clear();
}
    return 0;
}