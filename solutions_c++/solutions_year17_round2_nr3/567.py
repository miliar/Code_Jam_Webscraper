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
const double INF= 1000000000000.0;
const long double pi= acos(-1);
typedef long long int ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector< vector< int > > vvi;
const int MOD=1e9+7;
const ll LINF=0x3f3f3f3f3f3f3f3f;
double autonomia[105];
double resp[105];
int vel[105];
double d[105][105];
double dp[105][105];
int st,en;
int n,q;
const double eps = 1e-6;

void limpa()
{
  for(int i=0;i<n+5;i++)
  {
    resp[i]=10000000000000.0;
  }
}

void solve2()
{
  cin>>st>>en;
  limpa();
  resp[st]=0;
  priority_queue< pair<double,int> > pq;
  pq.push(mp(resp[st],st));
  while(!pq.empty())
  {
    pair<double,int> p = pq.top();
    pq.pop();
    int u=p.second;
    double c=-p.first;
    if(c>resp[u]+eps) continue;
    for(int i=1;i<=n;i++)
    {
      if(i==u) continue;
      if(autonomia[u]>=d[u][i])
      {
        double t=d[u][i]/vel[u];
        if(resp[i]>resp[u]+t)
        {
          resp[i]=resp[u]+t;
          pq.push(mp(-resp[i],i));
        }
      }
    }
  }
  cout<<resp[en];
}


void solve()
{
  cin>>n>>q;
  limpa();
  for(int i=1;i<=n;i++)
  {
    cin>>autonomia[i]>>vel[i];
  }

  for(int i=1;i<=n;i++)
  {
    for(int j=1;j<=n;j++)
    {
      cin>>d[i][j];
      if(d[i][j]==-1) d[i][j]=INF;
    }
  }
  for(int i=1;i<=n;i++) d[i][i]=0;
  for(int k=1;k<=n;k++)
  {
    for(int i=1;i<=n;i++)
    {
      for(int j=1;j<=n;j++)
      {
        d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
      }
    }
  }
  for(int i=0;i<q;i++)
  {
    if(i!=0) cout<<" ";
    solve2();
  }
  cout<<endl;
}


int main()
{
  cout<<setprecision(10)<<fixed;
  int tc;
  sc(tc);
  for(int t=1;t<=tc;t++)
  {
    printf("Case #%d: ",t);
    solve();
  }
  return 0;
}
