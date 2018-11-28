#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define ll long long


int main()
{
     freopen("tiii.in", "r", stdin);
  freopen("tiii.out", "w", stdout);
    ll t;
    cin>>t;
    cout<<setprecision(6)<<fixed;
    for(ll i=1;i<=t;i++)
    {
        double d;
        vector<double> v;
       ll n;
       cin>>d>>n;

       //Case #3: 33.333333

       for(int i=0;i<n;i++)
       {
           double pos,speed;
           cin>>pos>>speed;
           v.pb((d-pos)/speed);
       }
        sort(v.begin(),v.end());
       //cout<<maxi<<" ";
       cout<<"Case #"<<i<<": "<<d/v[n-1]<<endl;

    }
    return 0;
    }
