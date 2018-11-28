#include<bits/stdc++.h>
#define pb push_back
#define F first
#define S second
#define ll long long int
#define inf 1450000090
#define fastio ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define sd(x) scanf("%d",&x)
#define sd2(x,y) scanf("%d%d",&x,&y)
#define sdl(x) scanf("%lld",&x)
#define nax 100010
#define mp make_pair
#define MPI acos(-1)
#define sz(x) (int)(x.size())
#define pi pair <int , int>
#define pii pair < int , pair <int ,int > >
#define MOD 1000000007
using namespace std;
vector< pi > v;
int main(int argc, char const *argv[])
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t;
  sd(t);
  int r,h;
  for(int tt = 1;tt <= t;tt++)
  {
      ll fans = 0;
      v.clear();
      int n,k;
      sd2(n,k);
      printf("Case #%d: ",tt);
      for(int i = 1;i<=n;i++)
      {
        sd2(r,h);
        v.pb(mp(r,h));
      }
      sort(v.begin(), v.end());
      for(int i=n-1;i>=k-1;i--)
      {
          int rr = v[i].F;
          int hh = v[i].S;
          ll cans = rr*1ll*rr + 2*rr*1ll*hh;
          vector< ll > vals;
          for(int j=i-1;j>=0;j--)
          {
             vals.pb(-2*v[j].F*1ll*v[j].S);
          } 
          sort(vals.begin(), vals.end());
          for (int j = 0; j < k-1; ++j)
          {
              cans+=-1*vals[j];
          }
          fans = max(fans,cans);
      }
      double fans2 = fans * MPI;
      printf("%0.15lf\n", fans2);
  }
  return 0;
}  