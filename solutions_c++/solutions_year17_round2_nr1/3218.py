#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define mp make_pair
#define pd(t,n) printf("Case #%d: %lld\n",t,n)
#define ini(n) scanf("%d",&n)
#define inl(n) scanf("%lld",&n)
#define rf freopen("input.in", "r", stdin)
#define wf freopen("print1.txt", "w", stdout)
#define ii pair<ll,int>
#define f first
#define s second
#define pb push_back
#define maxx 200000
vector< pair <double,double>  > v;
double ans[10008];
int main()
{
 //rf;
 //wf;
  int t;
  ini(t);
  for(int tt=1;tt<=t;tt++)
  {
    v.clear();
    double d;
    int n;
    cin>>d>>n;
    for(int i=1;i<=n;i++)
    {
      double k,s;
      cin>>k>>s;
      v.pb(mp(k,s));
    }
    sort(v.begin(),v.end());
    int si=v.size();
    ans[si-1]=(d-v[si-1].f)/v[si-1].s;
    for(int i=si-2;i>=0;i--)
    {
         ans[i]=max(ans[i+1],(d-v[i].f)/v[i].s);
    }
    double print=d/ans[0];
    cout<<"Case #"<<tt<<": "<<fixed<<setprecision(7)<<print<<endl;

  }

  //system("pause");
}
