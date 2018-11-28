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
#define sz(x) (int)(x.size())
#define pi pair <int , int>
#define pii pair < int , pair <int ,int > >
#define MOD 1000000007
using namespace std;
multiset< int > sett;
int main(int argc, char const *argv[])
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t;
  sd(t);
  int n,k;
  for(int tt = 1;tt <= t;tt++)
  {
      sett.clear();
      printf("Case #%d: ",tt);
      sd2(n,k);// lite
      double u;
      double x;
      scanf("%lf",&u);
      int uu = (int)(10000*u+1e-6);
      int sum = 0;
      for(int i=1;i<=n;i++)
      {
         scanf("%lf",&x);
         int tt = (int)(x*10000+1e-6);
         sum+=tt;
         sett.insert(tt);
      }
      int tot = n*10000;
      while(sum < tot && uu!=0)
      {
          uu--;
          int item = *sett.begin();
          sett.erase(sett.find(item));
          item++;
          sett.insert(item);
          sum++;
      }
      double fans =  1;
      while(sz(sett)!=0)
      {
          int item = *sett.begin();
          sett.erase(sett.find(item));
          fans =  fans * 0.0001 * item;
      }
      printf("%0.15lf\n",fans);
  }
  return 0;
}  