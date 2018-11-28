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
std::vector< pi > v;
int main(int argc, char const *argv[])
{
  freopen("input.txt","read",stdin);
  freopen("output.txt","write",stdout);
  int t;
  sd(t);
  for(int tt=1;tt<=t;tt++)
  {
  	 printf("Case #%d: ",tt);
  	 int d,n;
  	 sd2(d,n);
  	 int a,b;
  	 v.clear();
  	 for(int i=1;i<=n;i++)
  	 {
  	 	sd2(a,b);
  	 	v.pb(mp(-a,b));
  	 }
  	 sort(v.begin(), v.end());
  	 double ma = -1;
  	 for(int i=0;i<n;i++)
  	 {
  	 	double val = (d-(v[i].F*(-1.00)))/v[i].S;
  	 	ma = max(ma,val);
  	 }
  	 double ans = d/ma;
  	 printf("%0.15lf\n",ans);
  }
  return 0;
}