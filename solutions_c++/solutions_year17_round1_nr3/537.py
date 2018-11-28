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
int hd,ad,hk,ak,b,d;

int get(int ds, int bs)
{
  int hdd=hd,add=ad,hkk=hk,akk=ak;
  int ret=0;
  int lastak=ak;
  for(int i=0;i<ds;i++)
  {
    if(ds>800) return INF;
    akk-=d;
    ret++;
    akk=max(akk,0);
    if(hdd<=akk)
    {
      akk=lastak;
      hdd=hd-akk;
      if(hdd<=0) return INF;
      ds++;
    }
    else hdd-=akk;
    lastak=akk;
  }
  for(int i=0;i<bs;i++)
  {
    if(bs>800) return INF;
    add+=b;
    ret++;
    if(hdd<=akk)
    {
      add-=b;
      hdd=hd-akk;
      if(hdd<=0) return INF;
      bs++;
    }
    else hdd-=akk;
  }
  while(hdd>0 and hkk>0)
  {
    ret++;
    if(ret>1000)
    {
      return INF;
    }
    hkk-=add;
    if(hkk<=0) break;
    if(hdd<=akk)
    {
      hdd=hd-akk;
      if(hdd<=0) return INF;
      hkk+=add;
    }
    else
    {
      hdd-=akk;
    }
  }
  if(hkk<=0) return ret;
  else return INF;
}

void solve()
{
  cin>>hd>>ad>>hk>>ak>>b>>d;
  int resp=INF;
  for(int i=0;i<=100;i++)
  {
    for(int j=0;j<=100;j++)
    {
      resp=min(resp,get(i,j));
    }
  }
  if(resp>=INF) cout<<"IMPOSSIBLE"<<endl;
  else cout<<resp<<endl;
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
