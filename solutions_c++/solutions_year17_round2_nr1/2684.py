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
#define MAXN 10003
ll a[MAXN];
vector<pair<ll,ll> >v;
double tim[MAXN];
int main()
{
  boost;
  freopen("in.txt","r",stdin); freopen("out.txt","w",stdout);
  int t;
  cin>>t;
  forup(tt,1,t+1)
  {
    v.clear();
    long long D,n,k,S;
    cin>>D>>n;
    forup(i,1,n+1)
    {
      cin>>k>>S;
      v.pb({k,S});
    }
    sort(v.rbegin(),v.rend());
    forup(i,0,n)
    {
      tim[i]=1.0*(D-v[i].fi)/v[i].se;
      if(!i)continue;
      tim[i]=max(tim[i-1],tim[i]);
    }
    //forup(i,0,n)cout<<tim[i]<<" ";
    //cout<<tim[n-1]<<endl;
    cout<<"Case #"<<tt<<": "<<fixed<<setprecision(9)<<1.0*D/tim[n-1]<<endl;
  }
  return 0;
}

