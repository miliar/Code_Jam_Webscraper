#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define fi first
#define se second
#define pb push_back
#define mp make_pair
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef pair<ll ,ll> ii;

int main()
{
   freopen("A-small-attempt0.in","r",stdin);
   freopen("A-small-attempt0_out.in","w",stdout);
   ll tst;
   double speed,dist,des,hor,time,n;
   vector<pair< double, pair<double,double> > > v;
   cin >> tst;
   for(int i=1;i<=tst;i++)
   {
       cin >> des>>n;
       for(ll j=1;j<=n;j++)
       {
          cin >> dist>>speed;
          time=(des-dist)/speed;
          v.pb(mp((des-dist),mp(speed,time)));
       }
       sort(v.begin(),v.end());
       time=v[0].se.se;
       for(ll j=0;j<v.size();j++)
       {
          if(j!=0)
          {
              if(v[j].se.se<time)
              {
                 time=v[j-1].se.se;
              }
              else
                 time=v[j].se.se;
          }
       }
       cout<<fixed;
       cout<<"Case #"<<i<<": "<<(des/time)<<"\n";
       v.clear();

   }
}
