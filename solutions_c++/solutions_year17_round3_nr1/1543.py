#include<bits/stdc++.h>
using namespace std;

#define fre freopen("in.txt","r",stdin)
#define ll long long
#define abs(x) ((x)>0?(x):-(x))
#define mod 1000000007
#define scand(x) scanf("%d",&x);
#define scanlld(x) scanf("%I64d",&x);
#define scans(x) scanf("%s",x);
#define printd(x) printf("%d",x);
#define printlld(x) printf("%I64d",x);
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define inf (1<<30)
#define forup(i,a,b) for(int i=a;i<b;i++)
#define pii pair<int,int>
#define boost ios_base::sync_with_stdio(0)
#define MAXN 1003
const double PI  =3.141592653589793238463;
ll a[MAXN];
multiset<double>s;
pair<double,double>v[MAXN];
int main()
{
  boost;
  //fre;
  freopen("in.txt","r",stdin); freopen("out.txt","w",stdout);
  int t;
  cin>>t;
  forup(tt,1,t+1)
  {
    int n,k;
    double ans=0;
    cin>>n>>k;
    forup(i,1,n+1)
      cin>>v[i].fi>>v[i].se;
    sort(v+1,v+n+1);
    s.clear();
    for(int i=1;i<=n;i++)
    {
      if(s.size()>=k-1)
      {
        double sum=0;
        int cnt=0;
        for(auto j:s)
        {
          if(cnt==k-1)break;
          cnt++,sum+=(-1.0*(j));
          //if(cnt==k-1)break;
        }   
        ans=max(ans,1.0*PI*v[i].fi*v[i].fi+2.0*PI*(sum+v[i].fi*v[i].se));
      }
      ans=max(ans,1.0*PI*v[i].fi*v[i].fi+2.0*PI*v[i].fi*v[i].se);
      s.insert(-1.0*v[i].fi*v[i].se);
    }
    cout<<"Case #"<<tt<<": "<<fixed<<setprecision(12)<<ans<<endl;
  }
  
  return 0;
}

