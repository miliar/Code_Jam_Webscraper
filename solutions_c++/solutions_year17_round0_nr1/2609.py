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

char rev(char c)
{
  if(c=='+') return '-';
  return '+';
}
void solve()
{
  string s;
  int k;
  cin>>s>>k;
  int ans=0;
  for(int i=0;i<=(int)s.size()-k;i++)
  {
    if(s[i]=='-')
    {
      ans++;
      for(int j=0;j<k and i+j<s.size();j++)
      {
        s[i+j]=rev(s[i+j]);
      }
    }
  }
  bool ok=true;
  for(int i=0;i<s.size();i++)
  {
    if(s[i]=='-')
    {
      ok=false;
      break;
    }
  }
  if(ok) cout<<ans<<endl;
  else cout<<"IMPOSSIBLE"<<endl;
}

int main()
{
  BUFF;
  int tc;
  cin>>tc;
  for(int t=1;t<=tc;t++)
  {
    cout<<"Case #"<<t<<": ";
    solve();
  }
  return 0;
}
