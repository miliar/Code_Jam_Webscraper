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
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector< vector< int > > vvi;
const int MOD=1e9+7;
const ll LINF=0x3f3f3f3f3f3f3f3f;
pair<int,char> colors[15];
int n;
char get(int i)
{
  if(i==0) return 'R';
  if(i==1) return 'O';
  if(i==2) return 'Y';
  if(i==3) return 'G';
  if(i==4) return 'B';
  if(i==5) return 'V';
}

bool ok(string &r)
{
  int tam=r.size();
  if(tam!=n) return false;
  if(tam==1) return true;
  for(int i=0;i<r.size();i++)
  {
    if(r[(i-1+n)%n]==r[i] or r[(i+1)%n]==r[i]) return false;
  }
  return true;
}

void solve()
{
  string resp;
  cin>>n;
  for(int i=0;i<6;i++)
  {
    cin>>colors[i].first;
    colors[i].second=get(i);
  }
  sort(colors,colors+6);
  reverse(colors,colors+6);
  if(colors[0].first>colors[1].first+colors[2].first)
  {
    cout<<"IMPOSSIBLE"<<endl;
    return ;
  }
  while(colors[1].first)
  {
    for(int i=0;i<2;i++)
    {
      resp.pb(colors[i].second);
      colors[i].first--;
    }
    cerr<<1<<endl;
  }
  while(colors[0].first)
  {
    resp.pb(colors[0].second);
    resp.pb(colors[2].second);
    colors[0].first--;
    colors[2].first--;
    cerr<<2<<endl;
  }
  while(colors[2].first)
  {
    cerr<<3<<endl;
    char c=colors[2].second;
    string tmp;
    tmp.pb(c);
    bool mudou=false;
    for(int i=0;i<(int)resp.size()-1;i++)
    {
      if(resp[i]!=c and resp[i+1]!=c)
      {
        mudou=true;
        colors[2].first--;
        resp=resp.substr(0,i+1)+tmp+resp.substr(i+1,resp.size()-i);
        break;
      }
    }
    if(!mudou) break;
  }
  if(colors[2].first)
  {
    if(resp[0]!=colors[2].second and resp[resp.size()-1]!=colors[2].second) resp.pb(colors[2].second);
  }
  cout<<resp<<endl;
}


int main()
{
  int tc;
  sc(tc);
  for(int t=1;t<=tc;t++)
  {
    printf("Case #%d: ",t);
    solve();
  }
  return 0;
}
