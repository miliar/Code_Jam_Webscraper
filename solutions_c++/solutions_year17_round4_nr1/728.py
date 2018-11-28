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
int cont[5];
int n,p;
void solve()
{
  memset(cont,0,sizeof(cont));
  cin>>n>>p;
  int resp=0;
  for(int i=0;i<n;i++)
  {
    int a;
    cin>>a;
    cont[a%p]++;
  }
  resp+=cont[0];
  cont[0]=0;
  for(int i=1;i<p;i++)
  {
    int v=min(cont[i],cont[p-i]);
    if(i==p-i)
    {
      resp+=v/2;
      cont[i]%=2;
    }
    else 
    {
      resp+=v;
      cont[i]-=v;
      cont[p-i]-=v;
    }
  }
  if(p==3)
  {
    int qte2=max(0,cont[2]/3);
    int qte1=max(0,cont[1]/3);
    resp+=qte1+qte2;
    cont[2]-=qte2*3;
    cont[1]-=qte1*3;
  }
  if(p==4)
  {
    if(cont[2]>0)
    {
      if(cont[1]>=2)
      {
        cont[1]-=2;
        cont[2]-=1;
        resp++;
      }
      else if(cont[3]>=2)
      {
        cont[3]-=2;
        cont[2]-=1;
      }
    }
    int qte3=max(0,cont[3]/4);
    int qte1=max(0,cont[1]/4);
    resp+=qte1+qte3;
    cont[3]-=qte3*4;
    cont[1]-=qte1*4;
  }
  for(int i=0;i<p;i++)
  {
    if(cont[i]>0)
    {
      resp+=1;
      break;
    }
  }
  assert(resp<=n and resp>=1);
  cout<<resp<<endl;
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
