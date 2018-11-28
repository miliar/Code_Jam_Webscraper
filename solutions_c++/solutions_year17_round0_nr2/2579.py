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

void solve()
{
  string num;
  cin>>num;
  string smallest(num.size(),'1');
  if(smallest>num)
  {
    string ans(num.size()-1,'9');
    cout<<ans<<endl;
    return;
  }
  int where=-1;
  for(int i=1;i<num.size();i++)
  {
    if(num[i]<num[i-1])
    {
      where=i;
      break;
    }
  }
  if(where==-1)
  {
    cout<<num<<endl;
    return;
  }
  for(int i=where-1;i>=0;i--)
  {
    if(i!=0 and num[i]>num[i-1])
    {
      num[i]--;
      where=i+1;
      break;
    }
    if(i==0)
    {
      num[i]--;
      where=i+1;
    }
  }
  for(int i=where;i<num.size();i++) num[i]='9';
  cout<<num<<endl;
}

int main()
{
  int tc;
  cin>>tc;
  for(int t=1;t<=tc;t++)
  {
    cout<<"Case #"<<t<<": ";
    solve();
  }
  return 0;
}
