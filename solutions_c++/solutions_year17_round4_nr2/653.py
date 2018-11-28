#include<bits/stdc++.h>
using namespace std;
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define pri(x) printf("%d\n", x)
#define mp make_pair
#define pb push_back
#define BUFF ios::sync_with_stdio(false);
#define imprime(v) for(int X=0;X<v.size();X++) printf("%d ", v[X]); printf("\n");
#define endl "\n"
const int INF= 0x3f3f3f3f;
const long double pi= acos(-1);
typedef long long int ll;
typedef long double ld;
typedef pair<int,ll> ii;
typedef vector<int> vi;
typedef vector< vector< int > > vvi;
const int MOD=1e9+7;
const ll LINF=0x3f3f3f3f3f3f3f3f;
int quantoscomprou[1005];
int n,c,m;
int compradosaqui[1005];
int resp;

bool ok(int rides)
{
  int sobrando=0;
  for(int i=n;i>=1;i--)
  {
    if(compradosaqui[i]<=rides)
    {
      sobrando-=(rides-compradosaqui[i]);
      sobrando=max(sobrando,0);
    }
    else
    {
      sobrando+=compradosaqui[i]-rides;
    }
  }
  return (sobrando==0);
}

int bb(int b, int e)
{
  if(b>=e) return b;
  int m=(b+e)/2;
  if(ok(m)) return bb(b,m);
  else return bb(m+1,e);
}

int gett(int rides)
{
  int ret=0;
  for(int i=n;i>=1;i--)
  {
    if(compradosaqui[i]>rides)
    {
      ret+=compradosaqui[i]-rides;
    }
  }
  return ret;
}

void solve()
{
  memset(compradosaqui,0,sizeof(compradosaqui));
  memset(quantoscomprou,0,sizeof(quantoscomprou));
  cin>>n>>c>>m;
  for(int i=0;i<m;i++)
  {
    int p,b;
    cin>>p>>b;
    quantoscomprou[b]++;
    compradosaqui[p]++;
  }
  int minr=0;
  int maxr=0;
  for(int i=1;i<=c;i++)
  {
    maxr+=quantoscomprou[i];
    minr=max(minr,quantoscomprou[i]);
  }
  minr=max(minr,(maxr+n-1)/n);
  resp=bb(minr,maxr);
  cout<<resp<<" "<<gett(resp)<<endl;
}


int main()
{
  int t;
  cin>>t;
  for(int tc=1;tc<=t;tc++)
  {
    cout<<"Case #"<<tc<<": ";
    solve();
  }
  return 0;
}
