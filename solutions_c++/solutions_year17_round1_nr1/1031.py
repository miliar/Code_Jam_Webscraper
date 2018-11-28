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

char grid[30][30];

void solve()
{
  int n,m;
  cin>>n>>m;
  for(int i=1;i<=n;i++)
  {
    for(int j=1;j<=m;j++)
    {
      cin>>grid[i][j];
    }
  }
  vector<bool> wait(30,false);
  for(int i=1;i<=n;i++)
  {
    char c='?';
    for(int j=1;j<=m;j++)
    {
      if(grid[i][j]!='?')
      {
        c=grid[i][j];
      }
      else if(c!='?') grid[i][j]=c;
    }
    if(c=='?') wait[i]=true;
    c='?';
    for(int j=m;j>=1;j--)
    {
      if(grid[i][j]!='?')
      {
        c=grid[i][j];
      }
      else if(c!='?') grid[i][j]=c;
    }
  }
  vector<char> aux(30,'?');
  for(int i=1;i<=n;i++)
  {
    if(wait[i])
    {
      if(aux[1]!='?')
      {
        wait[i]=false;
        for(int j=1;j<=m;j++)
        {
          grid[i][j]=aux[j];
        }

      }
    }
    else
    {
      for(int j=1;j<=m;j++) aux[j]=grid[i][j];
    }
  }

  aux.assign(30,'?');
  for(int i=n;i>=1;i--)
  {
    if(wait[i])
    {
      if(aux[1]!='?')
      {
        wait[i]=false;
        for(int j=1;j<=m;j++)
        {
          grid[i][j]=aux[j];
        }

      }
    }
    else
    {
      for(int j=1;j<=m;j++) aux[j]=grid[i][j];
    }
  }
  for(int i=1;i<=n;i++)
  {
    for(int j=1;j<=m;j++)
    {
      cout<<grid[i][j];
    }
    cout<<endl;
  }
}


int main()
{
  BUFF;
  int tc;
  cin>>tc;
  for(int t=1;t<=tc;t++)
  {
    cout<<"Case #"<<t<<":"<<endl;
    solve();
  }
  return 0;
}
