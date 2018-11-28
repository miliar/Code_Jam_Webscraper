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
priority_queue<ll int>q;
int main()
{
     ios::sync_with_stdio(0);
     ll int n,a,k;
     cin>>n;
     ll int caser=0;
     ll int count=0;
     
     for(int i=0;i<n;i++)
     { 
         while(q.size())
         q.pop();
         count=0;
         caser++;
         cin>>a>>k;
         q.push(a);
         while(1)
         {
             
             ll int r = q.top();
             
             if(r%2==0)
             {
                 count++;
                 if(r==0)
                 {q.push(0);
                 q.push(0);
                 }
                 else
                 {
                 q.push(r/2);
                 q.push(r/2-1);
                 }
                 
             }
             else
             {
                 count++;
                 q.push(r/2);
                 q.push(r/2);
             }
             if(count==k)
             {
                 if(r%2==0)
                 {
                     if(r==0)
                     cout<<"Case #"<<caser<<": "<<0<<" "<<0<<"\n";
                     else
                     {
                          cout<<"Case #"<<caser<<": "<<r/2<<" "<<r/2-1<<"\n";
                     }
                }
                else
                {
                    cout<<"Case #"<<caser<<": "<<r/2<<" "<<r/2<<"\n";
                }
                break;
             }
             q.pop();
         }
         
         
     }

    return 0;
}