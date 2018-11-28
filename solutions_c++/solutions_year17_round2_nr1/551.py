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
double tchegada[1005];
double k[1005];
double s[1005];
double d;
double get(int i)
{
  double daux=d-k[i];
  return daux/s[i];
}

void solve()
{
  int n,dd;
  sc2(dd,n);
  d=dd;
  for(int i=1;i<=n;i++)
  {
    int ki,si;
    sc2(ki,si);
    k[i]=ki;
    s[i]=si;
  }
  tchegada[n+1]=0.0;
  for(int i=n;i>=1;i--)
  {
    tchegada[i]=max(get(i),tchegada[i+1]);
  }
  double ans=d/tchegada[1];
  printf("%.10lf\n",ans);
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
