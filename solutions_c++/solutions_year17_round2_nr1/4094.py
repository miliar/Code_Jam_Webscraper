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
    vector<pair<ll int,ll int> >v;
    int main()
    {
         ios::sync_with_stdio(0);
         ll int t;
         cin>>t;
         ll int D,N,a,b;
         long double z,op;
         long double x,w,m;
 
         ll int flag=0;
         ll int tester=0;
         while(t--)
         {
             flag=0;
 
             cin>>D>>N;
             tester++;
             F(i,0,N-1)
             {
                 cin>>a>>b;
                 v.push_back(make_pair(a,b));
             }
             sort(v.begin(),v.end());
 
             if(v.size()==1)
             {
                 z = (long double)(D - v[0].first)/(long double)(v[0].second);
                 op = (long double)D/(long double)z;
                 cout<<"Case #"<<tester<<": "<<fixed<<setprecision(6)<<op<<"\n";
             }
             else
             {
                 x = (long double)(D - v[0].first)/(long double)(v[0].second);
                 for(int i=1;i<v.size();i++)
                 {
 
                     z = (long double)(D - v[i].first)/(long double)(v[i].second);
                     if(z>x)
                     {
                         x =z;
                     }
 
 
 
                 }
 
 
 
                 op = (long double)D/(long double)x;
                cout<<"Case #"<<tester<<": "<<fixed<<setprecision(6)<<op<<"\n";
 
             }
 
                  v.clear();
 
         }
        return 0;
    }